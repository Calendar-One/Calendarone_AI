import { configureAuth } from 'react-query-auth';
import { Navigate, useLocation } from 'react-router';
import { z } from 'zod';

import { ROUTES } from '@/config/router';
import { type TokenResponse } from '@/types/api/auth';
import { type User } from '@/types/api/users';

import { api } from './api-client';

// api call definitions for auth (types, schemas, requests):
// these are not part of features as this is a module shared across features

const getUser = async (): Promise<User | null> => {
  try {
    const response = await api.get('/users/me', {
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
    });

    return response.data;
  } catch (error) {
    if (error?.response?.status === 401) {
      localStorage.removeItem('accessToken');
    }
    return null;
  }
};

const logout = (): Promise<void> => {
  return api.post('/auth/logout');
};

const loginInputSchema = z.object({
  username: z.string().min(1, 'Required'),
  password: z.string().min(1, 'Required'),
});

type LoginInput = z.infer<typeof loginInputSchema>;

const loginApi = (data: LoginInput): Promise<TokenResponse> => {
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
): Promise<TokenResponse> => {
  return api.post('/auth/register', data);
};

const refreshApi = (refreshToken: string): Promise<TokenResponse> => {
  return api.post('/auth/refresh', { refresh_token: refreshToken });
};

const authConfig = {
  userFn: getUser,
  loginFn: async (data: LoginInput) => {
    const response = await loginApi(data);
    localStorage.setItem('accessToken', response.access_token);
    return response.user;
  },
  registerFn: async (data: RegisterInput) => {
    const response = await registerWithEmailAndPassword(data);
    localStorage.setItem('accessToken', response.access_token);
    return response.user;
  },
  logoutFn: async () => {
    localStorage.removeItem('accessToken');
    return await logout();
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

export const refreshAuth = async (failedRequest: any) => {
  const user = useUser();
  const newToken = await refreshApi(user?.data?.refresh_token || '');

  if (newToken) {
    failedRequest.response.config.headers.Authorization =
      newToken.token_type || 'Bearer' + ' ' + newToken.access_token;
    localStorage.setItem('accessToken', newToken.access_token);
    // you can set your token in storage too
    // setToken({ token: newToken });
    return Promise.resolve(newToken);
  } else {
    // you can redirect to login page here
    // router.push("/login");

    <Navigate to={ROUTES.auth.login.getHref(location.pathname)} replace />;

    return Promise.reject();
  }
};
