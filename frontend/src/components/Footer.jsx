import React from 'react';
import { Group, Text, Anchor } from '@mantine/core';

const Footer = () => {
  return (
    <footer className='bg-slate-900 border-t border-slate-700 px-6 py-4'>
      <div className='flex items-center justify-between'>
        <div className='flex items-center space-x-6'>
          <Text size='sm' className='text-slate-400'>
            © 2024 Calendarone AI. All rights reserved.
          </Text>
        </div>

        <Group gap='lg'>
          <Anchor
            href='#'
            size='sm'
            className='text-slate-400 hover:text-white transition-colors'
          >
            Privacy Policy
          </Anchor>
          <Anchor
            href='#'
            size='sm'
            className='text-slate-400 hover:text-white transition-colors'
          >
            Terms of Service
          </Anchor>
          <Anchor
            href='#'
            size='sm'
            className='text-slate-400 hover:text-white transition-colors'
          >
            Documentation
          </Anchor>
        </Group>
      </div>
    </footer>
  );
};

export default Footer;
