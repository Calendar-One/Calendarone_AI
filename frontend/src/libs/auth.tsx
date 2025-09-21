import { configureAuth } from 'react-query-auth';
import { Navigate, useLocation } from 'react-router';
import { z } from 'zod';
import { ROUTES } from '@/config/router';
import { type TokenResponse } from '@/types/api/auth';
import { type User } from '@/types/api/users';
import { api } from './api-client';
import type { ApiResponse } from '@/types/api';

// api call definitions for auth (types, schemas, requests):
// these are not part of features as this is a module shared across features
const getUserApi = async (): Promise<User | null> => {
  try {
    const response: ApiResponse<User> = await api.get('/users/me');
    return response.data ?? null;
  } catch (error) {
    console.error('Error getting user:', error);
    return null;
  }
};

const logoutApi = (): Promise<void> => {
  return api.post('/auth/logout');
};

const loginInputSchema = z.object({
  username: z.string().min(1, 'Required'),
  password: z.string().min(1, 'Required'),
});

type LoginInput = z.infer<typeof loginInputSchema>;

const loginApi = (data: LoginInput): Promise<ApiResponse<TokenResponse>> => {
  const formData = new URLSearchParams();
  formData.append('username', data.username);
  formData.append('password', data.password);

  return api.post('/auth/login', formData, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });
};

export const registerInputSchema = z
  .object({
    email: z.string().min(1, 'Required'),
    user_name: z.string().min(1, 'Required'),
    password: z.string().min(5, 'Required'),
  })
  .and(
    z
      .object({
        teamId: z.string().min(1, 'Required'),
        teamName: z.null().default(null),
      })
      .or(
        z.object({
          teamName: z.string().min(1, 'Required'),
          teamId: z.null().default(null),
        })
      )
  );

export type RegisterInput = z.infer<typeof registerInputSchema>;

const registerWithEmailAndPassword = (
  data: RegisterInput
): Promise<ApiResponse<TokenResponse>> => {
  return api.post('/auth/register', data);
};

const authConfig = {
  userFn: getUserApi,
  loginFn: async (data: LoginInput) => {
    const response = await loginApi(data);
    if (!response.data) {
      return null;
    }
    localStorage.setItem('accessToken', response.data?.access_token);
    localStorage.setItem('refreshToken', response.data?.refresh_token);
    return response.data?.user;
  },
  registerFn: async (data: RegisterInput) => {
    const response = await registerWithEmailAndPassword(data);
    if (!response.data) {
      return null;
    }
    localStorage.setItem('accessToken', response.data?.access_token);
    localStorage.setItem('refreshToken', response.data?.refresh_token);
    return response.data?.user;
  },
  logoutFn: async () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    return await logoutApi();
  },
};

export const { useUser, useLogin, useLogout, useRegister, AuthLoader } =
  configureAuth(authConfig);

export const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const user = useUser();
  const location = useLocation();

  if (!user.data) {
    return (
      <Navigate to={ROUTES.auth.login.getHref(location.pathname)} replace />
    );
  }

  return children;
};
