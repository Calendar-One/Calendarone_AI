import './App.css';
import Layout from './components/Layout.tsx';

function App() {
  return (

      <Layout>
        <div className='text-center py-20 bg-white dark:bg-gray-900'>
          <h1 className='text-4xl font-bold text-gray-900 dark:text-white mb-4'>
            Welcome to Calendarone AI
          </h1>
          <p className='text-gray-600 dark:text-gray-400 text-lg'>
            Your AI-powered calendar management platform
          </p>
        </div>
      </Layout>
  );
}

export default App;
