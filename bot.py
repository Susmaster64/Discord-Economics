import hikari

intents = hikari.Intents(hikari.Intents.ALL)
bot = hikari.GatewayBot(token='', intents=intents)
    
user_id_list = []

@bot.listen(hikari.DMMessageCreateEvent)
async def analCumSex(event):    
    
    if event.author_id in user_id_list:
        with open('balances.txt') as f:
            balances = list(f.read().split(','))
            
        contents = event.content.lower().strip()
        if contents == 'bal' or contents == 'balance':
            
            for n in range(len(user_id_list)):
                if user_id_list[n] == event.author_id:
                    output = balances[n]
                    break

            await event.author.send(f'Your current account balance is {output} :eggplant:s')
        
        elif list(event.content.lower().split(' '))[0] == 'send':
            try:
                transfer_amount = float(list(event.content.lower().split(' '))[1])
                for n in range(len(user_id_list)):
                    if user_id_list[n] == event.author_id:
                        output = balances[n]
                        index = n
                        break
                        print('y')
                
                if float(output) < transfer_amount:
                    await event.author.send('It\'s haram to be in debt')
                    print('y')
                    
                else:
                    if int(list(event.content.lower().split(' '))[2]) in user_id_list and int(list(event.content.lower().split(' '))[2]) != event.author_id:
                        print(list(event.content.lower().split(' '))[2])
                        print(list(event.content.lower().split(' '))[2])
                        new_bal = float(output) - float(list(event.content.lower().split(' '))[1])
                        user = await bot.rest.fetch_user(list(event.content.lower().split(" "))[2])
                        await event.author.send(f'Sending {transfer_amount} to {user}. \nYou currently have {output} :eggplant:s in your account. Making this transaction brings you down to {new_bal}')       
                        
                        balances[index] = str(new_bal)
                        with open('balances.txt', 'w') as f:
                            f.write(','.join(balances))         
                    else:
                        print(list(event.content.lower().split(' '))[2])
                        print(list(event.content.lower().split(' '))[2])
                        await event.author.send(f'You cannot send :eggplant:s to that user ID.')
                
                
            
            except Exception as exc:
                print(exc)
                await event.author.send('Amount to send *must* be a valid floating point number.')
        
        else:
            await event.author.send('Use `bal` or `balance` to check your balance. Use `send <send amount> <recipient\'s user ID>` to send someone some :eggplant:s')
        
bot.run()
