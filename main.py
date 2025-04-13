import os
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("user_session", api_id, api_hash)

exclude_titles = [
    "Super.Telegram",
    "BotFather",
    "J2TEAM Community",
    "Được Dev",
    "Telegram Apps Center",
    "Community",
    "Blum",
    "Telegram,",
    "Node.js Super",
    "ReactJs Super - Thảo luận - chém gió",
    "Deploy Super",
    "NextJs Super",
    "Telegram",
    "Mẹ",
    "Phạm Thị Ánh",
]


async def show_dialogs():
    dialogs = await client.get_dialogs()
    print(f"🔍 Tổng số cuộc trò chuyện: {len(dialogs)}\n")
    for dialog in dialogs:
        print(f"{dialog.name} - {dialog.id}")


async def delete_dialog_by_id(dialog_id):
    await client.delete_dialog(dialog_id)
    print(f"✅ Đã xóa cuộc trò chuyện có ID: {dialog_id}")


async def delete_excluded_dialogs():
    dialogs = await client.get_dialogs()
    dialogs_to_delete = [
        dialog
        for dialog in dialogs
        if not dialog.pinned
        and (dialog.folder_id is None or dialog.folder_id == 0)
        and dialog.name not in exclude_titles
    ]

    print(f"🔍 Tổng số cuộc trò chuyện sẽ bị xóa: {len(dialogs_to_delete)}\n")

    if dialogs_to_delete:
        print("Danh sách các cuộc trò chuyện sẽ bị xóa:")
        for dialog in dialogs_to_delete:
            print(f"{dialog.name} - {dialog.id}")

        confirmation = input(
            "\n🔴 Bạn có chắc chắn muốn xóa các cuộc trò chuyện này? Nhấn Enter để xác nhận hoặc Ctrl+C để hủy: "
        )

        if confirmation == "":
            print("✅ Đang xóa các cuộc trò chuyện đã chọn...")
            for dialog in dialogs_to_delete:
                await client.delete_dialog(dialog.id)
            print("✅ Đã xóa các cuộc trò chuyện!")
        else:
            print("❌ Quá trình xóa đã bị hủy.")
    else:
        print("Không có cuộc trò chuyện nào cần xóa.")


async def main():
    await client.start()
    print("✅ Đã đăng nhập bằng user account!")

    while True:
        print("\n--- MENU ---")
        print("1. Xuất tất cả các đoạn chat")
        print("2. Xóa chat theo ID")
        print("3. Xóa tất cả trừ các cuộc trò chuyện trong danh sách exclude_titles")
        print("4. Thoát")
        choice = input("Chọn hành động (1/2/3/4): ")

        if choice == "1":
            await show_dialogs()
        elif choice == "2":
            dialog_id = int(input("Nhập ID cuộc trò chuyện cần xóa: "))
            await delete_dialog_by_id(dialog_id)
        elif choice == "3":
            await delete_excluded_dialogs()
        elif choice == "4":
            print("🛑 Thoát chương trình...")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn lại.")

    print("✅ Hoàn thành!")


client.loop.run_until_complete(main())
