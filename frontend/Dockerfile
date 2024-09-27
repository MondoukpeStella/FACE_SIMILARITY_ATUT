FROM node as build-stage

WORKDIR /app
COPY package*.json ./
RUN npm install
# Update system
RUN apt-get update && apt-get upgrade  
  
COPY . .

# EXPOSE 5173
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]