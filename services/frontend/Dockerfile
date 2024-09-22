# Stage 1: Build Stage
FROM node:22-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package.json and pnpm-lock.yaml first
COPY package.json pnpm-lock.yaml* ./

# Install pnpm and dependencies
RUN apk add --no-cache npm && \
    npm install -g pnpm && \
    pnpm install --frozen-lockfile && \
    rm -rf /var/cache/apk/*

# Copy the rest of the application code
COPY . .

# Build the application
RUN pnpm run build

# Stage 2: Serve Stage
FROM nginx:stable-alpine

# Copy built files from the previous stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
