FROM python:2-alpine

MAINTAINER Yushin Washio <YWashio at EONERC dot RWTH-Aachen dot de>

RUN apk add --no-cache --virtual .fetch-deps \
		git \
	&& apk add --no-cache --virtual .build-deps \
		# needed for cffi
		libffi-dev \
		gcc \
		libc-dev \
		# needed for cryptography
		openssl-dev \
	&& git clone --depth 1 https://github.com/yuwash/nutgrass.git \
	&& cd nutgrass \
	&& pip install --no-cache-dir --upgrade -r requirements.txt \
	&& apk del .fetch-deps \
	&& apk del .build-deps
