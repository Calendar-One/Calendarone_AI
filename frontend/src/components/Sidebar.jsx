import React, { useState } from 'react';
import {
  TextInput,
  NavLink,
  Avatar,
  Menu,
  Text,
  Group,
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
    <aside className='w-64 bg-slate-900 border-r border-slate-700 h-full flex flex-col'>
      {/* Search */}
      <div className='p-4 border-b border-slate-700'>
        <TextInput
          placeholder='Q Go to...'
          leftSection={<IconSearch size={16} />}
          rightSection={
            <div className='text-xs text-slate-500 bg-slate-800 px-2 py-1 rounded'>
              Ctrl K
            </div>
          }
          styles={{
            input: {
              backgroundColor: '#1e293b',
              border: '1px solid #475569',
              color: '#e2e8f0',
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
                  : 'text-slate-300 hover:bg-slate-800 hover:text-white'
              }`}
              styles={{
                root: {
                  backgroundColor:
                    active === item.value ? '#2563eb' : 'transparent',
                  '&:hover': {
                    backgroundColor:
                      active === item.value ? '#2563eb' : '#1e293b',
                  },
                },
                label: {
                  color: active === item.value ? 'white' : '#cbd5e1',
                },
              }}
            />
          ))}
        </div>
      </nav>

      {/* User Profile */}
      <div className='p-4 border-t border-slate-700'>
        <Menu shadow='md' width={200} position='top-start'>
          <Menu.Target>
            <div className='flex items-center space-x-3 p-2 rounded-lg hover:bg-slate-800 cursor-pointer transition-colors'>
              <Avatar
                src='https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=40&h=40&fit=crop&crop=face'
                size='sm'
                radius='xl'
              />
              <div className='flex-1 min-w-0'>
                <Text size='sm' fw={500} className='text-white truncate'>
                  hao
                </Text>
                <Text size='xs' className='text-slate-400 truncate'>
                  skywalkeryin007@...
                </Text>
              </div>
              <ActionIcon variant='subtle' color='gray' size='sm'>
                <IconChevronDown size={14} />
              </ActionIcon>
            </div>
          </Menu.Target>

          <Menu.Dropdown className='bg-slate-800 border-slate-700'>
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
