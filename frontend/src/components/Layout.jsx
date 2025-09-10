import React from 'react';
import { AppShell } from '@mantine/core';
import Header from './Header';
import Sidebar from './Sidebar';
import Footer from './Footer';

const Layout = ({ children }) => {
  return (
    <AppShell
      header={{ height: 70 }}
      footer={{ height: 60 }}
      navbar={{ width: 256, breakpoint: 'sm' }}
      padding='md'
      className='bg-slate-950'
    >
      <AppShell.Header>
        <Header />
      </AppShell.Header>

      <AppShell.Navbar>
        <Sidebar />
      </AppShell.Navbar>

      <AppShell.Main className='bg-slate-950 min-h-screen'>
        <div className='p-6'>{children}</div>
      </AppShell.Main>

      <AppShell.Footer>
        <Footer />
      </AppShell.Footer>
    </AppShell>
  );
};

export default Layout;
