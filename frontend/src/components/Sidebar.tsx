import { useState } from 'react';
import {
  TextInput,
  NavLink,
  Avatar,
  Menu,
  Text,
  ActionIcon,
} from '@mantine/core';
import {
  IconSearch,
  IconGrid3x3,
  IconStar,
  IconSettings,
  IconHeadset,
  IconChevronDown,
  IconUser,
} from '@tabler/icons-react';

const Sidebar = () => {
  const [active, setActive] = useState('projects');

  const navigationItems = [
    {
      icon: IconGrid3x3,
      label: 'Projects',
      value: 'projects',
      description: 'Manage your projects',
    },
    {
      icon: IconStar,
      label: 'Upgrade',
      value: 'upgrade',
      description: 'Upgrade your plan',
    },
    {
      icon: IconSettings,
      label: 'Settings',
      value: 'settings',
      description: 'Configure your account',
    },
    {
      icon: IconHeadset,
      label: 'Support',
      value: 'support',
      description: 'Get help and support',
    },
  ];

  return (
    <aside className='w-64 h-full flex flex-col'>
      {/* Search */}
      <div className='p-4 border-b border-gray-200' style={{ height: '60px' }}>
        <TextInput
          placeholder='Q Go to...'
          leftSection={<IconSearch size={16} />}
          rightSectionWidth={50}
          rightSection={
            <div className='text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded w-full'>
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

      {/* Navigation */}
      <nav className='flex-1 p-4'>
        <div className='space-y-1'>
          {navigationItems.map(item => (
            <NavLink
              key={item.value}
              href='#'
              label={item.label}
              leftSection={<item.icon size={20} />}
              active={active === item.value}
              onClick={() => setActive(item.value)}
              className={`rounded-lg transition-colors ${
                active === item.value
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
              }`}
              styles={{
                root: {
                  backgroundColor:
                    active === item.value ? '#2563eb' : 'transparent',
                  '&:hover': {
                    backgroundColor:
                      active === item.value ? '#2563eb' : '#f3f4f6',
                  },
                },
                label: {
                  color: active === item.value ? 'white' : '#4b5563',
                },
              }}
            />
          ))}
        </div>
      </nav>

      {/* User Profile */}
      <div className='p-4 border-t border-gray-200'>
        <Menu shadow='md' width={200} position='top-start'>
          <Menu.Target>
            <div className='flex items-center space-x-3 p-2 rounded-lg hover:bg-gray-100 cursor-pointer transition-colors'>
              <Avatar
                src='https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=40&h=40&fit=crop&crop=face'
                size='sm'
                radius='xl'
              />
              <div className='flex-1 min-w-0'>
                <Text size='sm' fw={500} className='text-gray-900 truncate'>
                  hao
                </Text>
                <Text size='xs' className='text-gray-500 truncate'>
                  skywalkeryin007@...
                </Text>
              </div>
              <ActionIcon variant='subtle' color='gray' size='sm'>
                <IconChevronDown size={14} />
              </ActionIcon>
            </div>
          </Menu.Target>

          <Menu.Dropdown className='bg-white border-gray-200'>
            <Menu.Item leftSection={<IconUser size={16} />}>Profile</Menu.Item>
            <Menu.Item leftSection={<IconSettings size={16} />}>
              Settings
            </Menu.Item>
            <Menu.Divider />
            <Menu.Item color='red'>Sign out</Menu.Item>
          </Menu.Dropdown>
        </Menu>
      </div>
    </aside>
  );
};

export default Sidebar;
