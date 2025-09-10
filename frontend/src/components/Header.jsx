import React from 'react';
import { Button, Group, Select, ActionIcon } from '@mantine/core';
import { IconSettings, IconUser, IconPlus } from '@tabler/icons-react';

const Header = () => {
  return (
    <header className='bg-slate-900 border-b border-slate-700 px-6 py-4'>
      <div className='flex items-center justify-between'>
        {/* Left side - Logo and context */}
        <div className='flex items-center space-x-6'>
          <div className='flex items-center space-x-2'>
            <h1 className='text-xl font-semibold text-white'>Calendarone AI</h1>
            <span className='text-sm text-slate-400'>v1.0.0</span>
          </div>

          <div className='flex items-center space-x-2'>
            <span className='text-slate-300'>test</span>
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
                  border: '1px solid #475569',
                  color: '#e2e8f0',
                },
              }}
            />
          </div>
        </div>

        {/* Right side - Actions */}
        <Group gap='sm'>
          <ActionIcon
            variant='subtle'
            color='gray'
            size='lg'
            className='text-slate-400 hover:text-white hover:bg-slate-800'
          >
            <IconSettings size={20} />
          </ActionIcon>

          <ActionIcon
            variant='subtle'
            color='gray'
            size='lg'
            className='text-slate-400 hover:text-white hover:bg-slate-800'
          >
            <IconUser size={20} />
          </ActionIcon>

          <Button
            leftSection={<IconPlus size={16} />}
            size='sm'
            className='bg-blue-600 hover:bg-blue-700 text-white'
          >
            New project
          </Button>
        </Group>
      </div>
    </header>
  );
};

export default Header;
