FROM node:22-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the default Vite development port
EXPOSE 5173

# Serve the application on the default Vite port
CMD ["npm", "run", "dev", "--", "--host"]
