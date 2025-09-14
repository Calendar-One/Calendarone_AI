import { Button, Group, Select, ActionIcon } from '@mantine/core';
import { IconSettings, IconUser, IconPlus } from '@tabler/icons-react';
import DarkModeToggle from './DarkModeToggle';

const Header = () => {
  return (
    <>
      <div className='flex items-center justify-between h-full px-6 bg-white dark:bg-gray-900'>
        {/* Left side - Logo and context */}
        <div className='flex items-center space-x-6'>
          <div className='flex items-center space-x-2'>
            <span className='text-gray-600 dark:text-gray-300'>test</span>
            <Select
              placeholder='Hobby'
              data={[
                { value: 'hobby', label: 'Hobby' },
                { value: 'pro', label: 'Pro' },
                { value: 'enterprise', label: 'Enterprise' },
              ]}
              size='sm'
              className='w-24'
              styles={{
                input: {
                  backgroundColor: 'transparent',
                  border: '1px solid #d1d5db',
                  color: '#374151',
                },
              }}
            />
          </div>
        </div>

        {/* Right side - Actions */}
        <Group gap='sm'>
          <DarkModeToggle />
          <ActionIcon
            variant='subtle'
            color='gray'
            size='lg'
            className='text-gray-500 hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-gray-100 dark:hover:bg-gray-700'
          >
            <IconSettings size={20} />
          </ActionIcon>

          <ActionIcon
            variant='subtle'
            color='gray'
            size='lg'
            className='text-gray-500 hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-gray-100 dark:hover:bg-gray-700'
          >
            <IconUser size={20} />
          </ActionIcon>

          <Button
            leftSection={<IconPlus size={16} />}
            size='sm'
            className='bg-blue-600 hover:bg-blue-700 text-white dark:bg-red-600 dark:hover:bg-blue-700'
          >
            New project
          </Button>
        </Group>
      </div>
    </>
  );
};

export default Header;
