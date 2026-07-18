# Base image
FROM node:20.11.0-alpine AS base

# Builder step
FROM base AS builder

WORKDIR /exekaliburr/front

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

# Production step
FROM base AS production

WORKDIR /exekaliburr/front

COPY --from=builder /exekaliburr/front/public ./public
COPY --from=builder /exekaliburr/front/.next/standalone ./
COPY --from=builder /exekaliburr/front/.next/static ./.next/static

ENV NODE_ENV production
ENV HOSTNAME $FRONT_HOST

CMD ["node", "server.js"]
