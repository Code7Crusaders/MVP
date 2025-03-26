import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { createTheme } from '@mui/material/styles';
import { AppProvider } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import { useDemoRouter } from '@toolpad/core/internal';
import Chatbot from './components/Chatbot'; 
import AddCommentIcon from '@mui/icons-material/AddComment';
import ForumIcon from '@mui/icons-material/Forum';
import ChatIcon from '@mui/icons-material/Chat';
import MuccaSenzaSfondoIcon from './assets/muccasenzasfondo.png';
import 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import RichiestaSupporto from './components/RichiestaSupporto';
import Metriche from './components/Metriche';
import ContactSupportIcon from '@mui/icons-material/ContactSupport';
import EqualizerIcon from '@mui/icons-material/Equalizer';
import Templates from './components/Templates';
import AutoAwesomeMosaicIcon from '@mui/icons-material/AutoAwesomeMosaic';
import SupportAgentIcon from '@mui/icons-material/SupportAgent';
import { logout } from './utils/auth';


const NAVIGATION = [
  {
    segment: 'chatbot',
    title: 'Chatbot',
    icon: <AddCommentIcon />,
  },
  {
    segment: 'recent',
    title: 'Conversazioni salvate',
    icon: <ForumIcon />,
    children: [
      {
        segment: 'chat1',
        title: 'Chat 1',
        icon: <ChatIcon />,
      },
      {
        segment: 'chat2',
        title: 'Chat 2',
        icon: <ChatIcon />,
      },
    ],
  },
  {
    kind: 'divider',
  },
  {
    segment: 'support',
    title: 'Richiesta Supporto',
    icon: <ContactSupportIcon />,
  },
  {
    kind: 'divider',
  },
  {
    kind: 'header',
    title: 'Admin',
  },
  {
    segment: 'metrics',
    title: 'Visualizza Metriche',
    icon: <EqualizerIcon />,
  },
  {
    segment: 'templates',
    title: 'Gestione Templates',
    icon: <AutoAwesomeMosaicIcon />,
  },
  {
    segment: 'assistenza',
    title: 'Assistenza clienti',
    icon: <SupportAgentIcon />,
  },
];

const demoTheme = createTheme({
  cssVariables: {
    colorSchemeSelector: 'data-toolpad-color-scheme',
  },
  colorSchemes: { light: true, dark: true },
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 600,
      lg: 1200,
      xl: 1536,
    },
  },
});

function DashboardContent() {
  return (
    <Box sx={{ py: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
      <Typography>Chatbot</Typography>
    </Box>
  );
}

function OrdersContent() {
  return (
    <Box sx={{ py: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
      <Typography>Manage your orders here</Typography>
      <Chatbot />
    </Box>
  );
}

function Chat1Content() {
  return (
    <Chatbot chatId="chat1" />
  );
}

function Chat2Content() {
  return (
      <Chatbot chatId="chat2" /> 
  );
}

function SupportContent(){
  return (
    <RichiestaSupporto/>
  );
}

function MetricheContent(){
  return (
    <Metriche/>
  );
}

function TemplatesContent(){
  return (
    <Templates/>
  );
}

function AssistenzaContent(){
  return (
    <p>Assistenza</p>
  );
}

function DemoPageContent({ pathname }) {
  if (pathname === '/chatbot') {
    return <DashboardContent />;
  } else if (pathname === '/recent') {
    return <OrdersContent />;
  } else if (pathname === '/recent/chat1') {
    return <Chat1Content />;
  } else if (pathname === '/recent/chat2') {
    return <Chat2Content />;
  } else if (pathname === '/support'){
    return <SupportContent/>;
  } else if (pathname === '/metrics'){
    return <MetricheContent/>
  } else if (pathname === '/templates'){
    return <TemplatesContent/>
  } else if (pathname === '/assistenza'){
    return <AssistenzaContent/>
  }

  return (
    <Box sx={{ py: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
      <Typography>Page not found</Typography>
    </Box>
  );
}


DemoPageContent.propTypes = {
  pathname: PropTypes.string.isRequired,
};

function DashboardLayoutBranding(props) {
  const { window } = props;

  const [session, setSession] = React.useState(() => {
    const storedUser = localStorage.getItem('user');
    return {
      user: {
        name: storedUser ? JSON.parse(storedUser).name : 'User DiProva',
        email: storedUser ? JSON.parse(storedUser).email : 'email@example.com',
        image: 'https://as1.ftcdn.net/v2/jpg/03/46/83/96/1000_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg',
      },
    };
  });
  
  const navigate = useNavigate();

  const authentication = React.useMemo(() => ({
    signIn: () => {
      const storedUser = localStorage.getItem('user');
      if (storedUser) {
        const userData = JSON.parse(storedUser);
        setSession({
          user: {
            email: userData.email,
          },
        });
      }
    },
    signOut: () => {
      setSession(null);
      logout();
      navigate('/login');
    },
  }), []);

  const router = useDemoRouter('/chatbot');
  const demoWindow = window !== undefined ? window() : undefined;

  return (
    <AppProvider
      session={session}
      authentication={authentication}
      navigation={NAVIGATION}
      branding={{
        logo: <img src={MuccaSenzaSfondoIcon} alt="logo originale del Team di Sviluppo Code7Crusaders" />,
        title: 'Giorgione',
        homeUrl: '/chatbot',
        userDisplay: session?.user ? `${session.user.displayName} (${session.user.email})` : 'Guest', 
      }}
      router={router}
      theme={demoTheme}
      window={demoWindow}
    >
      <DashboardLayout>
        <DemoPageContent pathname={router.pathname} />
      </DashboardLayout>
    </AppProvider>
  );
}

export default DashboardLayoutBranding;
