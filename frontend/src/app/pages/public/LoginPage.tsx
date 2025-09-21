import { useState } from 'react';
import {
  Container,
  Paper,
  Title,
  Text,
  TextInput,
  PasswordInput,
  Button,
  Stack,
  Alert,
  Group,
  Anchor,
} from '@mantine/core';
import { IconAlertCircle, IconArrowLeft } from '@tabler/icons-react';
import { Link, useNavigate } from 'react-router';
import { useLogin } from '@/libs/auth';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate();

  const {
    mutate: loginMutate,
    error,
    isPending,
  } = useLogin({
    onSuccess: () => {
      navigate('/dashboard');
    },
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    loginMutate({ username: email, password });
  };

  return (
    <div className='min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800 flex items-center justify-center p-4'>
      <Container size='sm'>
        <Paper shadow='xl' p='xl' className='bg-white dark:bg-gray-800'>
          <Stack gap='md'>
            <div className='text-center'>
              <Title order={2} className='text-gray-900 dark:text-white mb-2'>
                Welcome Back
              </Title>
              <Text className='text-gray-600 dark:text-gray-300'>
                Sign in to your Calendarone AI account
              </Text>
            </div>

            {!!error && (
              <Alert
                icon={<IconAlertCircle size={16} />}
                color='red'
                variant='light'
              >
                {error?.response?.data?.message}
              </Alert>
            )}

            <form onSubmit={handleSubmit}>
              <Stack gap='md'>
                <TextInput
                  label='Email'
                  placeholder='Enter your email'
                  value={email}
                  onChange={e => setEmail(e.target.value)}
                  required
                  // type='email'
                  className='dark:text-white'
                />

                <PasswordInput
                  label='Password'
                  placeholder='Enter your password'
                  value={password}
                  onChange={e => setPassword(e.target.value)}
                  required
                  className='dark:text-white'
                />

                <Button
                  type='submit'
                  fullWidth
                  size='md'
                  loading={isPending}
                  className='bg-blue-600 hover:bg-blue-700'
                >
                  Sign In
                </Button>
              </Stack>
            </form>

            <Group justify='space-between' mt='md'>
              <Anchor
                component={Link}
                to='/register'
                size='sm'
                className='text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300'
              >
                Don't have an account? Sign up
              </Anchor>
              <Anchor
                component={Link}
                to='/'
                size='sm'
                className='text-gray-600 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300'
              >
                <Group gap='xs'>
                  <IconArrowLeft size={14} />
                  Back to Home
                </Group>
              </Anchor>
            </Group>

            {import.meta.env.DEV && (
              <div className='text-center mt-4 p-4 bg-gray-50 dark:bg-gray-700 rounded-lg'>
                <Text
                  size='sm'
                  className='text-gray-600 dark:text-gray-300 mb-2'
                >
                  Demo Credentials:
                </Text>
                <Text
                  size='sm'
                  className='text-gray-800 dark:text-gray-200 font-mono'
                >
                  Email: support@calendarone.com
                  <br />
                  Password: 123456sup
                </Text>
              </div>
            )}
          </Stack>
        </Paper>
      </Container>
    </div>
  );
};

export default LoginPage;
