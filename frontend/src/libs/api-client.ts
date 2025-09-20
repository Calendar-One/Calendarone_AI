import Axios, { type InternalAxiosRequestConfig } from 'axios';
import { notifications } from '@mantine/notifications';
import { env } from '@/config/env';
import { ROUTES } from '@/config/router';
import createAuthRefreshInterceptor from 'axios-auth-refresh';
import { refreshAuth } from './auth';

function authRequestInterceptor(config: InternalAxiosRequestConfig) {
  if (config.headers) {
    config.headers.Accept = 'application/json';
  }

  // config.withCredentials = true;
  return config;
}

export const api = Axios.create({
  baseURL: `${env.API_URL}/${env.API_VER}/`,
});

// export const setHeaderToken = (tokenType: string | null, token: string) => {
//   api.defaults.headers.common.Authorization = `${tokenType || 'Bearer'} ${token}`;
// };

// export const removeHeaderToken = () => {
//   //client.defaults.headers.common.Authorization = null;
//   delete api.defaults.headers.common.Authorization;
// };

api.interceptors.request.use(authRequestInterceptor);

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('accessToken');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// createAuthRefreshInterceptor(api, refreshAuth, {
//   statusCodes: [401], // default: [ 401 ]
//   shouldRefresh: error =>
//     error?.response?.data?.message === 'access token expired',
//   pauseInstanceWhileRefreshing: true,
// });

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
