import { createBrowserRouter, RouterProvider } from 'react-router';
import { MantineProvider } from '@mantine/core';
import { AuthProvider } from '@/contexts/AuthContext';
import ProtectedRoute from '@/components/Auth/ProtectedRoute';
import Layout from '@/components/Layouts/Layout';

// Import pages
import LandingPage from '@/app/pages/LandingPage';
import LoginPage from '@/app/pages/public/LoginPage';
import RegisterPage from '@/app/pages/public/RegisterPage';
import DashboardPage from '@/app/pages/DashboardPage';
import { Notifications } from '@mantine/notifications';

// Create router configuration
const router = createBrowserRouter([
  {
    path: '/',
    element: <LandingPage />,
  },
  {
    path: '/login',
    element: <LoginPage />,
  },
  {
    path: '/register',
    element: <RegisterPage />,
  },
  {
    path: '/dashboard',
    element: (
      <ProtectedRoute>
        <Layout>
          <DashboardPage />
        </Layout>
      </ProtectedRoute>
    ),
  },
  {
    path: '/profile',
    element: (
      <ProtectedRoute>
        <Layout>
          <div className='p-8'>
            <h1 className='text-2xl font-bold text-gray-900 dark:text-white'>
              Profile Page
            </h1>
            <p className='text-gray-600 dark:text-gray-300 mt-2'>
              This is a protected profile page.
            </p>
          </div>
        </Layout>
      </ProtectedRoute>
    ),
  },
  {
    path: '/settings',
    element: (
      <ProtectedRoute>
        <Layout>
          <div className='p-8'>
            <h1 className='text-2xl font-bold text-gray-900 dark:text-white'>
              Settings Page
            </h1>
            <p className='text-gray-600 dark:text-gray-300 mt-2'>
              This is a protected settings page.
            </p>
          </div>
        </Layout>
      </ProtectedRoute>
    ),
  },
  {
    path: '*',
    element: (
      <div className='min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900'>
        <div className='text-center'>
          <h1 className='text-4xl font-bold text-gray-900 dark:text-white mb-4'>
            404
          </h1>
          <p className='text-gray-600 dark:text-gray-300 mb-8'>
            Page not found
          </p>
          <a
            href='/'
            className='inline-block bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg transition-colors'
          >
            Go Home
          </a>
        </div>
      </div>
    ),
  },
]);

// Main Router Component
const AppRouter = () => {
  return (
    <MantineProvider>
      <Notifications />
      <AuthProvider>
        <RouterProvider router={router} />
      </AuthProvider>
    </MantineProvider>
  );
};

export default AppRouter;
