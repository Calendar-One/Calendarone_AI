import Axios, { type InternalAxiosRequestConfig } from 'axios';
import { notifications } from '@mantine/notifications';
import { env } from '@/config/env';
import { ROUTES } from '@/config/router';
import createAuthRefreshInterceptor from 'axios-auth-refresh';
import type { ApiResponse } from '@/types/api';
import axios from 'axios';

export const api = Axios.create({
  baseURL: `${env.API_URL}/${env.API_VER}/`,
});

function authRequestInterceptor(config: InternalAxiosRequestConfig) {
  if (config.headers) {
    config.headers.Accept = 'application/json';
  }

  config.withCredentials = true;
  return config;
}

api.interceptors.request.use(authRequestInterceptor);

api.interceptors.request.use(config => {
  const token = localStorage.getItem('accessToken');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// refresh token interceptor
export const refreshAuth = async (failedRequest: any) => {
  const refreshToken = localStorage.getItem('refreshToken');
  if (refreshToken) {
    const newTokenResponse = await axios.post('/auth/refresh', {
      refresh_token: refreshToken,
    });

    if (newTokenResponse.data && newTokenResponse.data.access_token) {
      failedRequest.response.config.headers.Authorization =
        newTokenResponse.data.token_type ||
        'Bearer' + ' ' + newTokenResponse.data.access_token;
      localStorage.setItem('accessToken', newTokenResponse.data.access_token);
      localStorage.setItem('refreshToken', newTokenResponse.data.refresh_token);

      return Promise.resolve();
    }
  } else {
    // you can redirect to login page here
    // <Navigate to={ROUTES.auth.login.getHref(location.pathname)} replace />;
    return Promise.reject();
  }
};

createAuthRefreshInterceptor(api, refreshAuth, {
  statusCodes: [401],
  shouldRefresh: error =>
    (error?.response?.data as ApiResponse<any>)?.message ===
    'access token expired',
  pauseInstanceWhileRefreshing: true,
});

// response interceptor
api.interceptors.response.use(
  response => {
    // intercept response data, for personalized handling
    const { data } = response as unknown as ApiResponse<any>;
    if (data?.isError === true) {
      console.log(data);
    }
    return data;
  },
  error => {
    const message =
      (error.response?.data as ApiResponse<any>)?.message || error.message;
    notifications.show({
      color: 'red',
      title: 'API Error',
      message: message,
    });

    if (error.response?.status === 401) {
      const location = window.location.pathname;
      if (location !== ROUTES.auth.login.path) {
        const searchParams = new URLSearchParams();
        const redirectTo =
          searchParams.get('redirectTo') || window.location.pathname;
        window.location.href = ROUTES.auth.login.getHref(redirectTo);
      }
    }

    return Promise.reject(error);
  }
);
