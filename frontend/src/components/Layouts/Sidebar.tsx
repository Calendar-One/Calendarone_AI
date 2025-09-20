import { useState } from 'react';
import {
  TextInput,
  NavLink,
  Avatar,
  Menu,
  Text,
  ActionIcon,
  Tooltip,
} from '@mantine/core';
import {
  IconSearch,
  IconGrid3x3,
  IconSettings,
  IconHeadset,
  IconChevronDown,
  IconUser,
} from '@tabler/icons-react';
import { useAppNavigation } from '@/hooks/useAppNavigation';
import { useUser, useLogout } from '@/libs/auth';

interface SidebarProps {
  collapsed: boolean;
}

const Sidebar = ({ collapsed }: SidebarProps) => {
  const { data: user } = useUser();
  const { mutate: logout } = useLogout();
  const nav = useAppNavigation();

  const handleLogout = () => {
    logout();
    nav.goToHome();
  };

  const [active, setActive] = useState('dashboard');

  const navigationItems = [
    {
      icon: IconGrid3x3,
      label: 'Dashboard',
      value: 'dashboard',
      description: 'View your calendar and events',
      to: nav.routes.app.dashboard.path,
    },
    {
      icon: IconUser,
      label: 'Profile',
      value: 'profile',
      description: 'Manage your profile',
      to: nav.routes.app.profile.path,
    },
    {
      icon: IconSettings,
      label: 'Settings',
      value: 'settings',
      description: 'Configure your account',
      to: nav.routes.app.settings.path,
    },
    {
      icon: IconHeadset,
      label: 'Support',
      value: 'support',
      description: 'Get help and support',
      to: '/support', // You can add this route later
    },
  ];

  return (
    <aside className='w-full h-full flex flex-col bg-white dark:bg-gray-900'>
      {/* Logo/ Title */}
      <div
        className={`p-4 border-b border-gray-200 dark:border-gray-700 ${
          collapsed ? 'flex justify-center' : ''
        }`}
        style={{ height: '60px' }}
      >
        {collapsed ? (
          <div
            className='flex items-center justify-center cursor-pointer'
            onClick={() => nav.goToDashboard()}
          >
            <span className='text-lg font-semibold text-gray-900 dark:text-white'>
              C
            </span>
          </div>
        ) : (
          <div
            className='flex items-center space-x-2 cursor-pointer'
            onClick={() => nav.goToDashboard()}
          >
            <span className='text-lg font-semibold text-gray-900 dark:text-white'>
              Calendarone AI
            </span>
            <span className='text-xs text-gray-500 dark:text-gray-400'>
              v1.0.0
            </span>
          </div>
        )}
      </div>

      {/* Search */}
      {!collapsed ? (
        <div
          className='p-4 border-gray-200 dark:border-gray-700'
          style={{ height: '60px' }}
        >
          <TextInput
            placeholder='Go to...'
            leftSection={<IconSearch size={16} />}
            rightSectionWidth={50}
            rightSection={
              <div className='text-xs text-gray-500 dark:text-gray-400 bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded w-full'>
                Ctrl K
              </div>
            }
            styles={{
              input: {
                backgroundColor: '#f9fafb',
                border: '1px solid #d1d5db',
                color: '#374151',
                '&:focus': {
                  borderColor: '#3b82f6',
                },
              },
            }}
          />
        </div>
      ) : (
        <div className={'p-2'}>
          <ActionIcon
            variant='subtle'
            color='gray'
            size='lg'
            onClick={() => {}}
          >
            <IconSearch size={20} />
          </ActionIcon>
        </div>
      )}

      {/* Navigation */}
      <nav className={`flex-1 ${collapsed ? 'p-2' : 'p-4'}`}>
        <div className='space-y-1'>
          {navigationItems.map(item => {
            if (collapsed) {
              return (
                <Tooltip key={item.value} label={item.label} position='right'>
                  <ActionIcon
                    variant={active === item.value ? 'filled' : 'subtle'}
                    color={active === item.value ? 'blue' : 'gray'}
                    size='lg'
                    onClick={() => {
                      setActive(item.value);
                      if (item.to) {
                        nav.push(item.to);
                      }
                    }}
                    // className={`w-full transition-colors ${
                    //   active === item.value
                    //     ? 'bg-blue-600 text-white'
                    //     : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900 dark:text-gray-300 dark:hover:bg-gray-800 dark:hover:text-white'
                    // }`}
                  >
                    <item.icon size={20} />
                  </ActionIcon>
                </Tooltip>
              );
            }

            return (
              <NavLink
                key={item.value}
                label={item.label}
                leftSection={<item.icon size={20} />}
                active={active === item.value}
                onClick={() => {
                  setActive(item.value);
                  if (item.to) {
                    nav.push(item.to);
                  }
                }}
                // className={`rounded-lg transition-colors ${
                //   active === item.value
                //     ? 'bg-blue-600 text-white'
                //     : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900 dark:text-gray-300 dark:hover:bg-gray-800 dark:hover:text-white'
                // }`}
              />
            );
          })}
        </div>
      </nav>

      {/* User Profile */}
      <div
        className={`${
          collapsed ? 'p-2' : 'p-4'
        } border-t border-gray-200 dark:border-gray-700`}
      >
        {collapsed ? (
          <Tooltip label={`${user?.user_name} (${user?.email})`} position='right'>
            <Menu shadow='md' width={200} position='top-start'>
              <Menu.Target>
                <div className='flex justify-center'>
                  <Avatar
                    src={
                  
                      'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=40&h=40&fit=crop&crop=face'
                    }
                    size='sm'
                    radius='xl'
                    className='cursor-pointer hover:ring-2 hover:ring-blue-500 transition-all'
                  />
                </div>
              </Menu.Target>

              <Menu.Dropdown className='bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700'>
                <Menu.Item
                  leftSection={<IconUser size={16} />}
                  onClick={() => nav.goToProfile()}
                >
                  Profile
                </Menu.Item>
                <Menu.Item
                  leftSection={<IconSettings size={16} />}
                  onClick={() => nav.goToSettings()}
                >
                  Settings
                </Menu.Item>

                <Menu.Divider />
                <Menu.Item color='red' onClick={handleLogout}>
                  Sign out
                </Menu.Item>
              </Menu.Dropdown>
            </Menu>
          </Tooltip>
        ) : (
          <Menu shadow='md' width={200} position='top-start'>
            <Menu.Target>
              <div className='flex items-center space-x-3 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 cursor-pointer transition-colors'>
                <Avatar
                  src={
          
                    'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=40&h=40&fit=crop&crop=face'
                  }
                  size='sm'
                  radius='xl'
                />
                <div className='flex-1 min-w-0'>
                  <Text
                    size='sm'
                    fw={500}
                    className='text-gray-900 dark:text-white truncate'
                  >
                    {user?.user_name}
                  </Text>
                  <Text
                    size='xs'
                    className='text-gray-500 dark:text-gray-400 truncate'
                  >
                    {user?.email}
                  </Text>
                </div>
                <ActionIcon variant='subtle' color='gray' size='sm'>
                  <IconChevronDown size={14} />
                </ActionIcon>
              </div>
            </Menu.Target>

            <Menu.Dropdown className='bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700'>
              <Menu.Item
                leftSection={<IconUser size={16} />}
                onClick={() => nav.goToProfile()}
              >
                Profile
              </Menu.Item>
              <Menu.Item
                leftSection={<IconSettings size={16} />}
                onClick={() => nav.goToSettings()}
              >
                Settings
              </Menu.Item>

              <Menu.Divider />
              <Menu.Item color='red' onClick={handleLogout}>
                Sign out
              </Menu.Item>
            </Menu.Dropdown>
          </Menu>
        )}
      </div>
    </aside>
  );
};

export default Sidebar;
