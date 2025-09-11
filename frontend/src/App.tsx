import './App.css';
import Layout from './components/Layout.tsx';

function App() {
  return (
    <Layout>
      <div className='text-center py-20'>
        <h1 className='text-4xl font-bold text-white mb-4'>
          Welcome to Calendarone AI
        </h1>
        <p className='text-slate-400 text-lg'>
          Your AI-powered calendar management platform
        </p>
      </div>
    </Layout>
  );
}

export default App;
