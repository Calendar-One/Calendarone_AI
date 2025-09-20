import { Button } from '@mantine/core';

export const MainErrorFallback = ({
  error,
  resetErrorBoundary,
}: {
  error: Error;
  resetErrorBoundary: () => void;
}) => {
  return (
    <div
      className='flex h-screen w-screen flex-col items-center justify-center text-red-500'
      role='alert'
    >
      <h2 className='text-lg font-semibold'>Ooops, something went wrong :( </h2>
      <pre>{error.message}</pre>
      <Button
        className='mt-4'
        onClick={() => window.location.assign(window.location.origin)}
      >
        Refresh
      </Button>
    </div>
  );
};
