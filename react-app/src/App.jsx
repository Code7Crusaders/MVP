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
import { useNavigate } from 'react-router-dom';
import RichiestaSupporto from './components/RichiestaSupporto';
import Metriche from './components/Metriche';
import ContactSupportIcon from '@mui/icons-material/ContactSupport';
import EqualizerIcon from '@mui/icons-material/Equalizer';
import Templates from './components/Templates';
import AutoAwesomeMosaicIcon from '@mui/icons-material/AutoAwesomeMosaic';
import SupportAgentIcon from '@mui/icons-material/SupportAgent';
import { logout } from './utils/auth';
import LoadChat from './components/LoadChat';
import Assistenza from './components/Assistenza';
import {jwtDecode} from 'jwt-decode'; // npm install jwt-decode
import Documenti from './components/Documenti';
import InsertDriveFileIcon from '@mui/icons-material/InsertDriveFile';

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
    <LoadChat />
  );
}

function SupportContent() {
  return <RichiestaSupporto />;
}

function MetricheContent() {
  return (
    <Metriche />
  );
}

function TemplatesContent() {
  return (
    <Templates />
  );
}

function AssistenzaContent() {
  return (
    <Assistenza />
  );
}

function DocumentiContent() {
  return (
    <Documenti />
  );
}

function DemoPageContent({ pathname, conversations }) {
  if (pathname === '/chatbot') {
    return <DashboardContent />;
  } else if (pathname.startsWith('/recent/chat-')) {
    const chatId = pathname.split('/recent/chat-')[1];
    console.log('Extracted chatId:', chatId); // Debugging log
    console.log('Conversations:', conversations); // Debugging log

    const conversation = conversations.find((conv) => String(conv.id) === chatId);

    if (!conversation) {
      console.error(`Chat with ID ${chatId} not found in conversations.`);
    }

    return conversation ? (
      <Chatbot chatId={chatId} chatTitle={conversation.title} />
    ) : (
      <Typography>Chat not found</Typography>
    );
  } else if (pathname === '/support') {
    return <SupportContent />;
  } else if (pathname === '/metrics') {
    return <MetricheContent />;
  } else if (pathname === '/templates') {
    return <TemplatesContent />;
  } else if (pathname === '/assistenza') {
    return <AssistenzaContent />;
  } else if (pathname === '/documenti') {
    return <DocumentiContent />;
  }

  return (
    <Box
      sx={{
        py: 4,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        textAlign: 'center',
      }}
    >
      <Typography>Page not found</Typography>
    </Box>
  );
}

DemoPageContent.propTypes = {
  pathname: PropTypes.string.isRequired,
  conversations: PropTypes.array.isRequired,
};

function DashboardLayoutBranding(props) {
  const { window } = props;

  const [session, setSession] = React.useState(() => {
    const storedUser = localStorage.getItem('user');
    return {
      user: {
        name: storedUser ? JSON.parse(storedUser).name : 'User DiProva',
        email: storedUser ? JSON.parse(storedUser).email : 'email@example.com',
      },
    };
  });

  const [conversations, setConversations] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [isAdmin, setIsAdmin] = React.useState(false); // Stato per verificare se l'utente è admin

  React.useEffect(() => {
    const fetchConversations = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await fetch('http://127.0.0.1:5001/conversation/get_all', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        const data = await response.json();
        console.log('Fetched conversations:', data); // Debugging log
        setConversations(data);
      } catch (error) {
        console.error('Failed to fetch conversations:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchConversations();
  }, []);

  React.useEffect(() => {
    const fetchAdminStatus = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await fetch('http://127.0.0.1:5001/is_admin', {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        const data = await response.json();
        if (response.ok) {
          setIsAdmin(data.is_admin); // Aggiorna lo stato in base alla risposta
        } else {
          console.error('Failed to fetch admin status:', data.error);
        }
      } catch (error) {
        console.error('Error fetching admin status:', error);
      }
    };

    fetchAdminStatus();
  }, []);

  const navigate = useNavigate();

  const authentication = React.useMemo(
    () => ({
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
    }),
    [navigate]
  );

  const router = useDemoRouter('/chatbot');
  const demoWindow = window !== undefined ? window() : undefined;

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
      children: conversations.map((conv) => ({
        segment: `chat-${conv.id}`,
        title: conv.title,
        icon: <ChatIcon />,
      })),
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
    ...(isAdmin // Mostra le voci admin solo se l'utente è amministratore
      ? [
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
        {
          segment: 'documenti',
          title: 'Gestione documenti',
          icon: <InsertDriveFileIcon />,
        },
      ]
      : []),
  ];

  if (loading) {
    return <Typography>Loading...</Typography>;
  }

  return (
    <AppProvider
      session={session}
      authentication={authentication}
      navigation={NAVIGATION}
      branding={{
        logo: <img src={MuccaSenzaSfondoIcon} alt="Team Code7Crusaders Logo" />,
        title: 'Giorgione',
        homeUrl: '/chatbot',
        userDisplay: session?.user ? `${session.user.name} (${session.user.email})` : 'Guest',
      }}
      router={router}
      theme={demoTheme}
      window={demoWindow}
    >
      <DashboardLayout>
        <DemoPageContent pathname={router.pathname} conversations={conversations} />
      </DashboardLayout>
    </AppProvider>
  );
}

DashboardLayoutBranding.propTypes = {
  window: PropTypes.func,
};

export default DashboardLayoutBranding;
