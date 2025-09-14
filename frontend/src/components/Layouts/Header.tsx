import { Group } from '@mantine/core';

import DarkModeToggle from './DarkModeToggle';

const Header = () => {
  return (
    <>
      <div className='flex items-center justify-between h-full px-6 bg-white dark:bg-gray-900 dark:border-gray-700'>
        {/* Left side - Logo and navigation */}
        <div className='flex items-center space-x-6'>
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
