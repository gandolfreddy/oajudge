
# input
mail_name = input().split('@')

# process
mail_name[0] = mail_name[0].replace('+', '')
mail_name[0] = mail_name[0].replace('-', '')
mail_name[0] = mail_name[0].replace('.', '')
new_mail_name = '@'.join(mail_name)

# output
print(new_mail_name)
