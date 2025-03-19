import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { createTheme } from '@mui/material/styles';
import DashboardIcon from '@mui/icons-material/Dashboard';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import DescriptionIcon from '@mui/icons-material/Description';  // Assicurati di importare DescriptionIcon
import { AppProvider } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import { useDemoRouter } from '@toolpad/core/internal';
import { useNavigate } from 'react-router-dom';
import Chatbot from './components/chatbot'; 

const NAVIGATION = [
  {
    segment: 'chatbot',
    title: 'Chatbot',
    icon: <DashboardIcon />,
  },
  {
    segment: 'recent',
    title: 'Conversazioni recenti',
    icon: <ShoppingCartIcon />,
    children: [
      {
        segment: 'chat1',
        title: 'Chat 1',
        icon: <DescriptionIcon />,
      },
      {
        segment: 'chat2',
        title: 'Chat 2',
        icon: <DescriptionIcon />,
      },
    ],
  },
  {
    kind: 'divider',
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

function DemoPageContent({ pathname }) {
  if (pathname === '/chatbot') {
    return <DashboardContent />;
  } else if (pathname === '/recent') {
    return <OrdersContent />;
  } else if (pathname === '/recent/chat1') {
    return <Chat1Content />;
  } else if (pathname === '/recent/chat2') {
    return <Chat2Content />;
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

  const router = useDemoRouter('/chatbot');
  const demoWindow = window !== undefined ? window() : undefined;

  return (
    <AppProvider
      navigation={NAVIGATION}
      branding={{
        logo: <img src="https://avatars.githubusercontent.com/u/185105956?s=200&v=4" alt="logo originale del Team di Sviluppo Code7Crusaders" />,
        title: 'Giorgione',
        homeUrl: '/chatbot',
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
