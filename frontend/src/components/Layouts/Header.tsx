import { Group, ActionIcon } from '@mantine/core';
import { IconLayoutSidebarLeftCollapse } from '@tabler/icons-react';

import DarkModeToggle from './DarkModeToggle';

interface HeaderProps {
  onToggleSidebar: () => void;
  sidebarCollapsed: boolean;
}

const Header = ({ onToggleSidebar, sidebarCollapsed }: HeaderProps) => {
  return (
    <>
      <div className='flex items-center justify-between h-full px-6 bg-white dark:bg-gray-900 dark:border-gray-700'>
        {/* Left side - Menu toggle and navigation */}
        <div className='flex items-center space-x-4'>
          <ActionIcon
            variant='subtle'
            color='gray'
            size='lg'
            onClick={onToggleSidebar}
            className='hover:bg-gray-100 dark:hover:bg-gray-800'
          >
            <IconLayoutSidebarLeftCollapse size={20} />
          </ActionIcon>

          {/* <Link to='/dashboard' className='flex items-center space-x-2'>
            <span className='text-xl font-bold text-gray-900 dark:text-white'>
              Calendarone AI
            </span>
          </Link> */}

          {/* <Group gap='xs'>
            <Button
              component={Link}
              to='/dashboard'
              variant='subtle'
              size='sm'
              leftSection={<IconDashboard size={16} />}
              className='text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white'
            >
              Dashboard
            </Button>
            <Button
              component={Link}
              to='/profile'
              variant='subtle'
              size='sm'
              leftSection={<IconUserCircle size={16} />}
              className='text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white'
            >
              Profile
            </Button>
          </Group> */}
        </div>

        {/* Right side - Actions */}
        <Group gap='sm'>
          <DarkModeToggle />

          {/* <Button
            leftSection={<IconPlus size={16} />}
            size='sm'
            className='bg-blue-600 hover:bg-blue-700 text-white'
          >
            New Event
          </Button> */}
        </Group>
      </div>
    </>
  );
};

export default Header;
