// // Define all available routes
// export const ROUTES = {
//   // Public routes
//   HOME: '/',
//   LOGIN: '/login',
//   REGISTER: '/register',

//   // Protected routes
//   DASHBOARD: '/dashboard',
//   PROFILE: '/profile',
//   SETTINGS: '/settings',

//   // 404 route
//   NOT_FOUND: '*',
// } as const;

export const ROUTES = {
  home: {
    path: '/',
    getHref: () => '/',
  },

  auth: {
    register: {
      path: '/auth/register',
      getHref: (redirectTo?: string | null | undefined) =>
        `/auth/register${
          redirectTo ? `?redirectTo=${encodeURIComponent(redirectTo)}` : ''
        }`,
    },
    login: {
      path: '/auth/login',
      getHref: (redirectTo?: string | null | undefined) =>
        `/auth/login${
          redirectTo ? `?redirectTo=${encodeURIComponent(redirectTo)}` : ''
        }`,
    },
  },

  app: {
    root: {
      path: '/app',
      getHref: () => '/app',
    },
    dashboard: {
      path: '/dashboard',
      getHref: () => '/app',
    },

    profile: {
      path: '/profile',
      getHref: () => '/app/profile',
    },

    settings: {
      path: '/settings',
      getHref: () => '/app/settings',
    },
  },
} as const;
