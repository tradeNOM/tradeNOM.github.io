from pypresence import Presence
import time

client_id = '911619459104505896'
RPC = Presence(client_id)

def connect_rpc(retries=3, delay=5):
    for attempt in range(1, retries + 1):
        try:
            RPC.connect()
            print("✅ Connected to Discord RPC")
            return True
        except Exception as e:
            print(f"⚠️ Attempt {attempt} failed to connect: {e}")
            time.sleep(delay)
    return False

def update_presence():
    try:
        RPC.update(
            details="closed",
            state="Just go to https://tradenom.github.io",
            large_image="logo",
            large_text="Our store",
            buttons=[{"label": "Check the store out!", "url": "https://tradenom.github.io"}],
            start=time.time()
        )
        print("✅ Presence updated successfully")
        return True
    except Exception as e:
        print(f"⚠️ Failed to update presence: {e}")
        return False

if __name__ == "__main__":
    if connect_rpc():
        if update_presence():
            try:
                while True:
                    time.sleep(15)
            except KeyboardInterrupt:
                print("\nExiting gracefully...")
        else:
            print("Presence update failed, exiting.")
    else:
        print("Could not connect to Discord RPC after multiple attempts, exiting.")
