import { Group, Text, Anchor } from '@mantine/core';

const Footer = () => {
  return (
    <footer className='bg-gray-50 border-t border-gray-200 px-6 py-4 dark:bg-gray-800 dark:border-gray-700'>
      <div className='flex items-center justify-between'>
        <div className='flex items-center space-x-6'>
          <Text size='sm' className='text-gray-500 dark:text-gray-400'>
            © 2024 Calendarone AI. All rights reserved.
          </Text>
        </div>

        <Group gap='lg'>
          <Anchor
            href='#'
            size='sm'
            className='text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-100 transition-colors'
          >
            Privacy Policy
          </Anchor>
          <Anchor
            href='#'
            size='sm'
            className='text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-100 transition-colors'
          >
            Terms of Service
          </Anchor>
          <Anchor
            href='#'
            size='sm'
            className='text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-100 transition-colors'
          >
            Documentation
          </Anchor>
        </Group>
      </div>
    </footer>
  );
};

export default Footer;
