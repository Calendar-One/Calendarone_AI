// Define all available routes
export const ROUTES = {
  // Public routes
  HOME: '/',
  LOGIN: '/login',
  REGISTER: '/register',

  // Protected routes
  DASHBOARD: '/dashboard',
  PROFILE: '/profile',
  SETTINGS: '/settings',

  // 404 route
  NOT_FOUND: '*',
} as const;
