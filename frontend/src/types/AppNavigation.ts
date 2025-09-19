import { ROUTES } from '../config/router';

// Type for route keys
export type RouteKey = keyof typeof ROUTES;

// Type for route values
export type RoutePath = (typeof ROUTES)[RouteKey];

// Navigation functions interface
export interface NavigationFunctions {
  // Route constants for easy access
  routes: typeof ROUTES;

  // Public routes
  goToHome: () => void;
  goToLogin: () => void;
  goToRegister: () => void;

  // Protected routes
  goToDashboard: () => void;
  goToProfile: () => void;
  goToSettings: () => void;

  // Utility functions
  goBack: () => void;
  goForward: () => void;
  replace: (path: string) => void;
  push: (path: string) => void;

  // Navigation with state
  goToLoginWithReturnUrl: (returnUrl?: string) => void;
  goToDashboardWithState: (state?: any) => void;
}

// Route validation utility
// export const isValidRoute = (path: string): path is RoutePath => {
//   return Object.values(ROUTES).includes(path as RoutePath);
// };

// // Get route name from path
// export const getRouteName = (path: string): string => {
//   const routeEntries = Object.entries(ROUTES);
//   const routeEntry = routeEntries.find(([, routePath]) => routePath.path === path);
//   return routeEntry ? routeEntry[0] : 'UNKNOWN';
// };

// // Check if route is public (doesn't require authentication)
// export const isPublicRoute = (path: string): boolean => {
//   const publicRoutes: string[] = [ROUTES.HOME, ROUTES.LOGIN, ROUTES.REGISTER];
//   return publicRoutes.includes(path);
// };

// Check if route is protected (requires authentication)
export const isProtectedRoute = (path: string): boolean => {
  const protectedRoutes: string[] = [
    ROUTES.app.dashboard.path,
    ROUTES.app.profile.path,
    ROUTES.app.settings.path,
  ];
  return protectedRoutes.includes(path);
};

// Navigation constants for easy reference
export const NAVIGATION = {
  ROUTES,
  // isValidRoute,
  // getRouteName,
  // isPublicRoute,
  isProtectedRoute,
} as const;
