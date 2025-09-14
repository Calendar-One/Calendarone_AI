import { useNavigate } from 'react-router';
import { ROUTES } from '../config/router';
import type { NavigationFunctions } from '../types/AppNavigation';

// Custom hook that provides navigation functions
export const useAppNavigation = () : NavigationFunctions => {
  const navigate = useNavigate();

  return {
    routes: ROUTES,
    // Public routes
    goToHome: () => navigate(ROUTES.HOME),
    goToLogin: () => navigate(ROUTES.LOGIN),
    goToRegister: () => navigate(ROUTES.REGISTER),

    // Protected routes
    goToDashboard: () => navigate(ROUTES.DASHBOARD),
    goToProfile: () => navigate(ROUTES.PROFILE),
    goToSettings: () => navigate(ROUTES.SETTINGS),

    // Utility functions
    goBack: () => navigate(-1),
    goForward: () => navigate(1),
    replace: (path: string) => navigate(path, { replace: true }),
    push: (path: string) => navigate(path),

    // Navigation with state
    goToLoginWithReturnUrl: (returnUrl?: string) => {
      navigate(ROUTES.LOGIN, {
        state: { from: returnUrl || window.location.pathname },
      });
    },
    goToDashboardWithState: (state?: any) => {
      navigate(ROUTES.DASHBOARD, { state });
    },
  };
};

export default useAppNavigation;
