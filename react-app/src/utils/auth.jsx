export const getToken = () => {
    return localStorage.getItem('token');
};
  
export const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
};
  
export const isAuthenticated = () => {
    return !!getToken();
};
  