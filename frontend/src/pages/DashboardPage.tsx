import { 
  Container, 
  Title, 
  Text, 
  Grid, 
  Card, 
  Group, 
  Button, 
  Stack,
  Badge,
  Avatar,
  ActionIcon
} from '@mantine/core';
import { 
  IconCalendar, 
  IconPlus, 
  IconSettings, 
  IconBell,
  IconClock,
  IconUsers
} from '@tabler/icons-react';
import { useAuth } from '../contexts/AuthContext';

const DashboardPage = () => {
  const { user } = useAuth();

  // Mock data for demonstration
  const upcomingEvents = [
    { id: 1, title: 'Team Meeting', time: '10:00 AM', type: 'meeting' },
    { id: 2, title: 'Project Review', time: '2:00 PM', type: 'review' },
    { id: 3, title: 'Client Call', time: '4:30 PM', type: 'call' },
  ];

  const recentActivity = [
    { id: 1, action: 'Created new event', time: '2 hours ago' },
    { id: 2, action: 'Updated schedule', time: '5 hours ago' },
    { id: 3, action: 'Shared calendar', time: '1 day ago' },
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Container size="xl" className="py-8">
        {/* Header */}
        <div className="mb-8">
          <Group justify="space-between" align="center">
            <div>
              <Title order={1} className="text-gray-900 dark:text-white">
                Welcome back, {user?.name}!
              </Title>
              <Text className="text-gray-600 dark:text-gray-300">
                Here's what's happening with your calendar today.
              </Text>
            </div>
            <Group gap="sm">
              <ActionIcon variant="subtle" color="gray" size="lg">
                <IconBell size={20} />
              </ActionIcon>
              <ActionIcon variant="subtle" color="gray" size="lg">
                <IconSettings size={20} />
              </ActionIcon>
              <Button
                leftSection={<IconPlus size={16} />}
                className="bg-blue-600 hover:bg-blue-700"
              >
                New Event
              </Button>
            </Group>
          </Group>
        </div>

        {/* Stats Cards */}
        <Grid className="mb-8">
          <Grid.Col span={{ base: 12, sm: 6, md: 3 }}>
            <Card shadow="sm" padding="lg" className="bg-white dark:bg-gray-800">
              <Group justify="space-between">
                <div>
                  <Text size="sm" className="text-gray-600 dark:text-gray-300">
                    Today's Events
                  </Text>
                  <Text size="xl" fw={700} className="text-gray-900 dark:text-white">
                    5
                  </Text>
                </div>
                <IconCalendar size={32} className="text-blue-600 dark:text-blue-400" />
              </Group>
            </Card>
          </Grid.Col>

          <Grid.Col span={{ base: 12, sm: 6, md: 3 }}>
            <Card shadow="sm" padding="lg" className="bg-white dark:bg-gray-800">
              <Group justify="space-between">
                <div>
                  <Text size="sm" className="text-gray-600 dark:text-gray-300">
                    This Week
                  </Text>
                  <Text size="xl" fw={700} className="text-gray-900 dark:text-white">
                    23
                  </Text>
                </div>
                <IconClock size={32} className="text-green-600 dark:text-green-400" />
              </Group>
            </Card>
          </Grid.Col>

          <Grid.Col span={{ base: 12, sm: 6, md: 3 }}>
            <Card shadow="sm" padding="lg" className="bg-white dark:bg-gray-800">
              <Group justify="space-between">
                <div>
                  <Text size="sm" className="text-gray-600 dark:text-gray-300">
                    Team Members
                  </Text>
                  <Text size="xl" fw={700} className="text-gray-900 dark:text-white">
                    12
                  </Text>
                </div>
                <IconUsers size={32} className="text-purple-600 dark:text-purple-400" />
              </Group>
            </Card>
          </Grid.Col>

          <Grid.Col span={{ base: 12, sm: 6, md: 3 }}>
            <Card shadow="sm" padding="lg" className="bg-white dark:bg-gray-800">
              <Group justify="space-between">
                <div>
                  <Text size="sm" className="text-gray-600 dark:text-gray-300">
                    AI Suggestions
                  </Text>
                  <Text size="xl" fw={700} className="text-gray-900 dark:text-white">
                    3
                  </Text>
                </div>
                <IconBell size={32} className="text-orange-600 dark:text-orange-400" />
              </Group>
            </Card>
          </Grid.Col>
        </Grid>

        {/* Main Content */}
        <Grid>
          <Grid.Col span={{ base: 12, md: 8 }}>
            <Card shadow="sm" padding="lg" className="bg-white dark:bg-gray-800 mb-6">
              <Title order={3} className="text-gray-900 dark:text-white mb-4">
                Upcoming Events
              </Title>
              <Stack gap="md">
                {upcomingEvents.map((event) => (
                  <div
                    key={event.id}
                    className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-3 h-3 bg-blue-600 rounded-full"></div>
                      <div>
                        <Text fw={500} className="text-gray-900 dark:text-white">
                          {event.title}
                        </Text>
                        <Text size="sm" className="text-gray-600 dark:text-gray-300">
                          {event.time}
                        </Text>
                      </div>
                    </div>
                    <Badge
                      color={event.type === 'meeting' ? 'blue' : event.type === 'review' ? 'green' : 'purple'}
                      variant="light"
                    >
                      {event.type}
                    </Badge>
                  </div>
                ))}
              </Stack>
            </Card>
          </Grid.Col>

          <Grid.Col span={{ base: 12, md: 4 }}>
            <Card shadow="sm" padding="lg" className="bg-white dark:bg-gray-800">
              <Title order={3} className="text-gray-900 dark:text-white mb-4">
                Recent Activity
              </Title>
              <Stack gap="md">
                {recentActivity.map((activity) => (
                  <div key={activity.id} className="flex items-center gap-3">
                    <Avatar size="sm" color="blue" />
                    <div className="flex-1">
                      <Text size="sm" className="text-gray-900 dark:text-white">
                        {activity.action}
                      </Text>
                      <Text size="xs" className="text-gray-600 dark:text-gray-300">
                        {activity.time}
                      </Text>
                    </div>
                  </div>
                ))}
              </Stack>
            </Card>
          </Grid.Col>
        </Grid>
      </Container>
    </div>
  );
};

export default DashboardPage;
