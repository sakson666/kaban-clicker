import flet as ft
import asyncio


async def main(page: ft.Page) -> None:
    page.title = "Kaban Clicker"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#141221"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.fonts = {"Fulbo Argenta": "fonts/Fulbo Argenta.ttf"}
    page.theme = ft.Theme(font_family="Fulbo Argenta")

    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.95

        score_counter.opacity = 50
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.left = event.local_x
        score_counter.top = event.local_y
        score_counter.bottom = 0

        progress_bar.value += (1/100)

        if score.data % 100 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="🐗+100",
                    size=20,
                    color="#794519",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#25223a"
            )
            page.snack_bar.open= True
            progress_bar.value = 0

        await page.update_async()

        await asyncio.sleep(0.1)
        image.scale = 1
        score_counter.opacity = 0

        await page.update_async()

    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="kabanch.png",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color="#794519",
        bgcolor="#59381c"
    )

    page.add(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=8000)


