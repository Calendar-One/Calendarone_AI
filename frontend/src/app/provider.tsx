import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import * as React from 'react';
import { ErrorBoundary } from 'react-error-boundary';
import { Notifications } from '@mantine/notifications';
import { Loader } from '@mantine/core';
import { AuthLoader } from '@/libs/auth';
import { queryConfig } from '@/libs/react-query';
import { MantineProvider } from '@mantine/core';
import { MainErrorFallback } from '@/components/errors/main';

type AppProviderProps = {
  children: React.ReactNode;
};

export const AppProvider = ({ children }: AppProviderProps) => {
  const [queryClient] = React.useState(
    () =>
      new QueryClient({
        defaultOptions: queryConfig,
      })
  );

  return (
    <React.Suspense
      fallback={
        <div className='flex h-screen w-screen items-center justify-center'>
          <Loader />
        </div>
      }
    >
      <ErrorBoundary FallbackComponent={MainErrorFallback}>
        <QueryClientProvider client={queryClient}>
          {/* React Query Devtools */}
          {import.meta.env.DEV && <ReactQueryDevtools />}
          <MantineProvider>
            <Notifications />
            <AuthLoader
              renderLoading={() => (
                <div className='flex h-screen w-screen items-center justify-center'>
                  <Loader />
                </div>
              )}
              renderError={(error) => (
                <MainErrorFallback
                  error={error as Error}
                  resetErrorBoundary={() => {}}
                />
              )}
            >
              {children}
            </AuthLoader>{' '}
          </MantineProvider>
        </QueryClientProvider>
      </ErrorBoundary>
    </React.Suspense>
  );
};
