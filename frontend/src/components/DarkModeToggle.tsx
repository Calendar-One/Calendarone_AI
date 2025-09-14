import {
  ActionIcon,
  useMantineColorScheme,
} from '@mantine/core';
import { IconSun, IconMoon } from '@tabler/icons-react';
import { useEffect } from 'react';


const DarkModeToggle = () => {
  const { setColorScheme, colorScheme, toggleColorScheme } =
    useMantineColorScheme();

  // Initialize dark mode and listen for system preference changes
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

    const handleChange = (e: MediaQueryListEvent) => {
      setColorScheme(e.matches ? 'dark' : 'light');
    };

    // Listen for changes to system preference
    mediaQuery.addEventListener('change', handleChange);

    // Cleanup listener on unmount
    return () => {
      mediaQuery.removeEventListener('change', handleChange);
    };
  }, []);

  return (
    <ActionIcon
      variant='subtle'
      color='gray'
      size='lg'
      onClick={toggleColorScheme}
      className='text-gray-500 hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-700'
      aria-label={
        colorScheme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'
      }
    >
      {colorScheme === 'dark' ? <IconSun size={20} /> : <IconMoon size={20} />}
    </ActionIcon>
  );
};

export default DarkModeToggle;
