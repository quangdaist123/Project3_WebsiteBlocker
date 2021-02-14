import tkinter as tk
# -------------------


def block():
    host_file = r"C:\Windows\System32\drivers\etc\hosts"
    loopback_ip_addr = '127.0.0.1'
    website_to_block = txt_list.get(1.0, tk.END).split(sep='\n')
    # Remove empty string resulting from the "get" method
    website_to_block = list(filter(None, website_to_block))
    with open('hosts', 'a+') as f:
        for website in website_to_block:
            f.write(loopback_ip_addr + ' ' + website + '\n')
            f.write(loopback_ip_addr + ' www.' + website + '\n')
        # Show message
        status.set("Okeeee")


def unblock():
    host_file = r"C:\Windows\System32\drivers\etc\hosts"
    website_to_block = txt_list.get(1.0, tk.END).split(sep='\n')
    # Remove empty string resulting from the "get" method
    website_to_block = list(filter(None, website_to_block))
    # Change the file path to host_file to actually block websites. Run this script with administrator privilege
    with open('hosts', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if not any(website in line for website in website_to_block):
                f.write(line)
        f.truncate()
        # Show message
        status.set("Unblocked everything")



window = tk.Tk()
window.title('Blocker')
# -------------------
frm_1 = tk.Frame(master=window)

block_list = ['facebook.com', 'youtube.com']
lb_list = tk.Label(master=frm_1, text="List to block:")
txt_list = tk.Text(master=frm_1, width=20, height=12)
block_list_str = '\n'.join(block_list)
txt_list.insert(1.0, block_list_str)
lb_list.pack(anchor='nw')
txt_list.pack(fill=tk.BOTH)

# Chưa cần thêm chức năng hẹn giờ
'''
btn_from = tk.Label(master=frm_1, text="From: ")
ent_from = tk.Entry(master=frm_1, width=10)
btn_to = tk.Label(master=frm_1, text="To:")
ent_to = tk.Entry(master=frm_1, width=10)

btn_from.pack(side='left')
ent_from.pack(side='left')
btn_to.pack(side='left')
ent_to.pack(side='left')
'''

frm_1.pack(padx=5, fill=tk.BOTH)
# -------------------
frm_2 = tk.Frame(master=window)

btn_block = tk.Button(master=frm_2, bg='blue', text="Block", command=block)
btn_unblock = tk.Button(master=frm_2, bg='red', text="Unblock", command=unblock)

btn_block.pack(side='left', expand=True, anchor='e', padx=1)
btn_unblock.pack(side='left', expand=True, anchor='w', padx=1)

frm_2.pack(padx=5, pady=5, fill=tk.BOTH)
# -------------------
status = tk.StringVar()
lbl_status = tk.Label(master=window, fg='green', textvariable=status)
lbl_status.pack(padx=5, anchor='n', fill=tk.BOTH)


window.mainloop()
