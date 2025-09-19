import { useNavigate } from 'react-router';
import { ROUTES } from '../config/router';
import type { NavigationFunctions } from '../types/AppNavigation';

// Custom hook that provides navigation functions
export const useAppNavigation = (): NavigationFunctions => {
  const navigate = useNavigate();

  return {
    routes: ROUTES,
    // Public routes
    goToHome: () => navigate(ROUTES.home.path),
    goToLogin: () => navigate(ROUTES.auth.login.path),
    goToRegister: () => navigate(ROUTES.auth.register.path),

    // Protected routes
    goToDashboard: () => navigate(ROUTES.app.dashboard.path),
    goToProfile: () => navigate(ROUTES.app.profile.path),
    goToSettings: () => navigate(ROUTES.app.settings.path),

    // Utility functions
    goBack: () => navigate(-1),
    goForward: () => navigate(1),
    replace: (path: string) => navigate(path, { replace: true }),
    push: (path: string) => navigate(path),

    // Navigation with state
    goToLoginWithReturnUrl: (returnUrl?: string) => {
      navigate(ROUTES.auth.login.path, {
        state: { from: returnUrl || window.location.pathname },
      });
    },
    goToDashboardWithState: (state?: any) => {
      navigate(ROUTES.app.dashboard.path, { state });
    },
  };
};

export default useAppNavigation;
