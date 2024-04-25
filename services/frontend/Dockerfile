FROM node:21-alpine

WORKDIR /app

RUN npm install -g pnpm

COPY package.json .

RUN pnpm install

COPY . .
RUN pnpm run build
EXPOSE 5173

CMD [ "pnpm", "run", "preview" ]