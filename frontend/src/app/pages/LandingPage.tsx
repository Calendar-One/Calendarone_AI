import { Button, Container, Title, Text, Group, Stack } from '@mantine/core';
import { IconCalendar, IconBrain, IconArrowRight } from '@tabler/icons-react';
import { Link } from 'react-router';

const LandingPage = () => {
  return (
    <div className='min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800'>
      <Container size='lg' className='py-20'>
        <Stack align='center' gap='xl'>
          {/* Hero Section */}
          <div className='text-center'>
            <Title
              order={1}
              size='4rem'
              className='text-gray-900 dark:text-white mb-6'
            >
              Calendarone AI
            </Title>
            <Text
              size='xl'
              className='text-gray-600 dark:text-gray-300 mb-8 max-w-2xl mx-auto'
            >
              Your AI-powered calendar management platform that helps you stay
              organized, productive, and never miss important events.
            </Text>
            <Group justify='center' gap='md'>
              <Button
                component={Link}
                to='/login'
                size='lg'
                rightSection={<IconArrowRight size={16} />}
                className='bg-blue-600 hover:bg-blue-700'
              >
                Get Started
              </Button>
              <Button
                component={Link}
                to='/register'
                variant='outline'
                size='lg'
                className='border-blue-600 text-blue-600 hover:bg-blue-50 dark:border-blue-400 dark:text-blue-400 dark:hover:bg-blue-900/20'
              >
                Sign Up
              </Button>
            </Group>
          </div>

          {/* Features Section */}
          <div className='grid grid-cols-1 md:grid-cols-3 gap-8 mt-16 w-full'>
            <div className='text-center p-6 bg-white dark:bg-gray-800 rounded-lg shadow-lg'>
              <IconCalendar
                size={48}
                className='text-blue-600 dark:text-blue-400 mx-auto mb-4'
              />
              <Title order={3} className='text-gray-900 dark:text-white mb-2'>
                Smart Scheduling
              </Title>
              <Text className='text-gray-600 dark:text-gray-300'>
                AI-powered scheduling that finds the perfect time for your
                meetings and events.
              </Text>
            </div>

            <div className='text-center p-6 bg-white dark:bg-gray-800 rounded-lg shadow-lg'>
              <IconBrain
                size={48}
                className='text-blue-600 dark:text-blue-400 mx-auto mb-4'
              />
              <Title order={3} className='text-gray-900 dark:text-white mb-2'>
                AI Assistant
              </Title>
              <Text className='text-gray-600 dark:text-gray-300'>
                Intelligent calendar assistant that learns your preferences and
                optimizes your schedule.
              </Text>
            </div>

            <div className='text-center p-6 bg-white dark:bg-gray-800 rounded-lg shadow-lg'>
              <IconCalendar
                size={48}
                className='text-blue-600 dark:text-blue-400 mx-auto mb-4'
              />
              <Title order={3} className='text-gray-900 dark:text-white mb-2'>
                Seamless Integration
              </Title>
              <Text className='text-gray-600 dark:text-gray-300'>
                Connect with your favorite calendar apps and productivity tools.
              </Text>
            </div>
          </div>
        </Stack>
      </Container>
    </div>
  );
};

export default LandingPage;
