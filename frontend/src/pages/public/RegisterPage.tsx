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
import { useAuth } from '../../contexts/AuthContext';

const RegisterPage = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    if (password.length < 6) {
      setError('Password must be at least 6 characters long');
      return;
    }

    setIsLoading(true);

    try {
      const success = await register(name, email, password);
      if (success) {
        navigate('/dashboard');
      } else {
        setError('Registration failed. Please try again.');
      }
    } catch (err) {
      setError('An error occurred during registration');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className='min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800 flex items-center justify-center p-4'>
      <Container size='sm'>
        <Paper shadow='xl' p='xl' className='bg-white dark:bg-gray-800'>
          <Stack gap='md'>
            <div className='text-center'>
              <Title order={2} className='text-gray-900 dark:text-white mb-2'>
                Create Account
              </Title>
              <Text className='text-gray-600 dark:text-gray-300'>
                Join Calendarone AI and start managing your schedule
                intelligently
              </Text>
            </div>

            {error && (
              <Alert
                icon={<IconAlertCircle size={16} />}
                color='red'
                variant='light'
              >
                {error}
              </Alert>
            )}

            <form onSubmit={handleSubmit}>
              <Stack gap='md'>
                <TextInput
                  label='Full Name'
                  placeholder='Enter your full name'
                  value={name}
                  onChange={e => setName(e.target.value)}
                  required
                  className='dark:text-white'
                />

                <TextInput
                  label='Email'
                  placeholder='Enter your email'
                  value={email}
                  onChange={e => setEmail(e.target.value)}
                  required
                  type='email'
                  className='dark:text-white'
                />

                <PasswordInput
                  label='Password'
                  placeholder='Create a password'
                  value={password}
                  onChange={e => setPassword(e.target.value)}
                  required
                  className='dark:text-white'
                />

                <PasswordInput
                  label='Confirm Password'
                  placeholder='Confirm your password'
                  value={confirmPassword}
                  onChange={e => setConfirmPassword(e.target.value)}
                  required
                  className='dark:text-white'
                />

                <Button
                  type='submit'
                  fullWidth
                  size='md'
                  loading={isLoading}
                  className='bg-blue-600 hover:bg-blue-700'
                >
                  Create Account
                </Button>
              </Stack>
            </form>

            <Group justify='space-between' mt='md'>
              <Anchor
                component={Link}
                to='/login'
                size='sm'
                className='text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300'
              >
                Already have an account? Sign in
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
          </Stack>
        </Paper>
      </Container>
    </div>
  );
};

export default RegisterPage;
