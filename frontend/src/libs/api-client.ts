import Axios, { type InternalAxiosRequestConfig } from 'axios';

import { notifications } from '@mantine/notifications';
import { env } from '@/config/env';
import { ROUTES } from '@/config/router';

function authRequestInterceptor(config: InternalAxiosRequestConfig) {
  if (config.headers) {
    config.headers.Accept = 'application/json';
  }

  config.withCredentials = true;
  return config;
}

export const api = Axios.create({
  baseURL: `${env.API_URL}/${env.API_VER}/`,
});

api.interceptors.request.use(authRequestInterceptor);
api.interceptors.response.use(
  response => {
    return response.data;
  },
  error => {
    const message = error.response?.data?.message || error.message;
    notifications.show({
      color: 'red',
      title: 'Notification with custom styles',
      message: message,
    });

    if (error.response?.status === 401) {
      const searchParams = new URLSearchParams();
      const redirectTo =
        searchParams.get('redirectTo') || window.location.pathname;
      window.location.href = ROUTES.auth.login.getHref(redirectTo);
    }

    return Promise.reject(error);
  }
);
