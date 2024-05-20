.PHONY: start-app-desktop start-app-web start-app-ios build-app-ios

# デスクトップアプリ起動
make start-app-desktop:
	cd app && poetry run flet run -d -r

# Webアプリ起動
make start-app-web:
	cd app && poetry run flet run --web -d -r

# IOSアプリ起動
make start-app-ios:
	cd app && poetry run flet run --ios -d -r

make build-app-web:
	cd app && poetry run flet build web

make build-app-ios:
	cd app && poetry run flet build ipa

make docker-build:
	cd app && docker build -t flet-env-image .

make docker-run:
	cd app && docker run -p 8000:8000 flet-env-image