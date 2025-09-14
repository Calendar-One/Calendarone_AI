import React from 'react';
import { AppShell } from '@mantine/core';
import Header from './Header.tsx';
import Sidebar from './Sidebar.tsx';
// import Footer from './Footer.tsx';

const Layout = ({ children }: { children: React.ReactNode }) => {
  return (
    <AppShell
      layout='alt'
      header={{ height: 60 }}
      footer={{ height: 60 }}
      navbar={{ width: 256, breakpoint: 'sm' }}
      // aside={{ width: 0, breakpoint: 'sm' }}
      padding='md'
      className='bg-white dark:bg-slate-900'
    >
      <AppShell.Header>
        <Header />
      </AppShell.Header>

      <AppShell.Navbar>
        <Sidebar />
      </AppShell.Navbar>

      <AppShell.Main>
        <>{children}</>
      </AppShell.Main>

      {/* <AppShell.Footer>
        <Footer />
      </AppShell.Footer> */}
    </AppShell>
  );
};

export default Layout;
