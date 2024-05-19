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