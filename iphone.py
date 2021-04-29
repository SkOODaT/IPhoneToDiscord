# Python 3.7
import discord
import subprocess
from discord.utils import get
import plistlib
from pyipa import IPAparser
from uuid import uuid4
import os
#import json

Client = discord.Client()
ClientToken = ''

IDeviceMobileDir = 'IDeviceMobile/'
IOSDeviceSupportDir = 'IOSDeviceSupport/' 
IPAFile = 'GDS-4.2R2.ipa'  # Signed IPA

AdminUser = 110522349201246488 # UserID
BotChannel = 837083793562945410 # ChannelID

# TODO
# subprocess function
# config.json settings


devices = {
         #'NAME':'UDID',
         'iphone73':'',
         'iphonese1':'',
         'iphonese2':'',
         'iphonese3':'',
         'iphonese4':'',
         'iphonese5':'',
         'iphonese6':'',
         'iphonese7':'',
         'iphonese8':'',
         'iphonese9':'',
         'iphonese10':'',
         'iphonese11':'',
         'iphone71':'',
         'iphone72':'',
         'iphone6s1':'',
         'iphone6s2':''
         }

devimg = {
         'iphone73':IOSDeviceSupportDir+'IOS-14.4/DeveloperDiskImage.dmg',
         'iphonese1':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese2':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese3':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese4':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese5':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese6':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese7':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese8':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese9':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese10':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphonese11':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphone71':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphone72':IOSDeviceSupportDir+'IOS-13.4/DeveloperDiskImage.dmg',
         'iphone6s1':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg',
         'iphone6s2':IOSDeviceSupportDir+'IOS-12.3/DeveloperDiskImage.dmg'
        }

devsig = {
         'iphone73':IOSDeviceSupportDir+'IOS-14.4/DeveloperDiskImage.dmg.signature',
         'iphonese1':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese2':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese3':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese4':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese5':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese6':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese7':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese8':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese9':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese10':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphonese11':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphone71':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphone72':IOSDeviceSupportDir+'IOS-13.4/DeveloperDiskImage.dmg.signature',
         'iphone6s1':IOSDeviceSupportDir+'IOS-13.7/DeveloperDiskImage.dmg.signature',
         'iphone6s2':IOSDeviceSupportDir+'IOS-12.3/DeveloperDiskImage.dmg.signature'
         }

def parse_ipa(ipa_path):
    ipa_parser = IPAparser(ipa_path)
    info = ipa_parser.parseInfo()
    bundle_id = info["CFBundleIdentifier"]
    version = info["CFBundleShortVersionString"]
    return bundle_id, version 

@Client.event
async def on_message(message):
    try:
        # Ignore Self
        if message.author == Client.user:
            return
        # Log Attempts 
        print(str(message.author) + ' Tried To Run A Command.')
        # Only Admins 
        if message.author.id != AdminUser:
            return
        # Only In Channel
        if message.channel.id != BotChannel:
            return
        # Help Info
        if message.content.startswith('!help'):
            #await message.channel.send(devices)
            await message.channel.send('```\nCommands:\n\n' +
                                        '**Dont Forget To Mount Dev Image** \n\n' +
                                        '!list - List all devices. \n' +
                                        '!mount <IPHONE> - Mount IOS dev image. \n' +
                                        '!batt <IPHONE> - Show battery info. \n'
                                        '!carrier <IPHONE> - Show carrier info. \n' +
                                        '!versionios <IPHONE> - Show IOS version.  \n' +
                                        '!reboot <IPHONE> - Reboot the IOS device. \n' +
                                        '!screen <IPHONE> - Screen shot the IOS devcie. \n' +
                                        '!startpogo <IPHONE> - Force start Pokemon Go. \n' +
                                        '!versionpogo <IPHONE> - Show Pokemon Go version. \n' +
                                        '!ipainfo - Show information on directory IPA. \n' +
                                        '!installpogo <IPHONE> - Install Pokemon Go Onto Device.```'
                                        )
        # Device List 
        if message.content.startswith('!list'):
            iphones = ''
            for d in devices:
                iphones += d + '\n'
            print(iphones)
            await message.channel.send('```\n'+iphones+'```')
        # Device Infos Debug
        if message.content.startswith('!info'):
            args = message.content.split(" ")
            MyOut = subprocess.Popen([IDeviceMobileDir+'ideviceinfo', '-u', devices.get(args[1]), ''],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            print(stdout.decode("utf-8"))
            #await message.channel.send('```'+stdout.decode("utf-8")+'```')
        # Mount Disk Image For Advanced Functions Like Screen Shots
        if message.content.startswith('!mount'):
            args = message.content.split(" ")
            MyOut = subprocess.Popen([IDeviceMobileDir+'ideviceimagemounter', '-u', devices.get(args[1]), devimg.get(args[1]), devsig.get(args[1])],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            print(stdout.decode("utf-8"))
            await message.channel.send('```\n'+stdout.decode("utf-8")+'```')
        # Device Batt
        if message.content.startswith('!batt'):
            args = message.content.split(" ")
            MyOut = subprocess.Popen([IDeviceMobileDir+'ideviceinfo', '-u', devices.get(args[1]), '-q', 'com.apple.mobile.battery'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            print(stdout)
            await message.channel.send('```\n'+stdout.decode("utf-8")+'```')
        # Device Carrier
        if message.content.startswith('!carrier'):
            args = message.content.split(" ")
            MyOut = subprocess.Popen([IDeviceMobileDir+'ideviceinfo', '-u', devices.get(args[1]), '-k', 'CarrierBundleInfoArray'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            await message.channel.send('```\n'+stdout.decode("utf-8")+'```')
        # Device Version
        if message.content.startswith('!versionios'):
            args = message.content.split(" ")
            MyOut = subprocess.Popen([IDeviceMobileDir+'ideviceinfo', '-u', devices.get(args[1]), '-k', 'ProductVersion'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            await message.channel.send('```\nIOS Version: '+stdout.decode("utf-8")+'```')
        # Device Reboot
        if message.content.startswith('!reboot'):
            args = message.content.split(" ")
            MyOut = subprocess.Popen([IDeviceMobileDir+'idevicediagnostics', '-u', devices.get(args[1]), 'restart'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            print(stdout.decode("utf-8"))
            await message.channel.send(stdout.decode("utf-8"))
        # Device Screenshot
        if message.content.startswith('!screen'):
            args = message.content.split(" ")
            MyOut = subprocess.Popen([IDeviceMobileDir+'idevicescreenshot', '-u', devices.get(args[1]), args[1]+'.png'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            print(stdout.decode("utf-8"))
            await message.channel.send('```\n'+stdout.decode("utf-8")+'```', file=discord.File(args[1]+'.png'))
        # Startup Pokemon Go
        if message.content.startswith('!startpogo'):
            args = message.content.split(" ")
            MyOut = subprocess.Popen([IDeviceMobileDir+'idevicedebug', '-u', devices.get(args[1]), 'run', 'com.nianticlabs.pokemongo'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            #print(stdout.decode("utf-8"))
            await message.channel.send('```\n'+'Started Pokemon Go'+'```')
        # Pokemon Go Installed Version 
        if message.content.startswith('!versionpogo'):
            args = message.content.split(" ")
            MyOut = subprocess.Popen([IDeviceMobileDir+'ideviceinstaller', '-u', devices.get(args[1]), '-l', '-o', 'xml'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            plist = plistlib.loads(stdout)
            for items in plist:
                await message.channel.send('```\n'+items.get('CFBundleName')+' Version: '+items.get('CFBundleShortVersionString')+'```')
        # IPA Information
        if message.content.startswith('!ipainfo'):
            bundle_id, version = parse_ipa(IPAFile)
            print(version, bundle_id)
            await message.channel.send('```\nDirectory IPA Information:\n'+bundle_id+'\n'+version+'```')
        # Pokemon Go Install
        if message.content.startswith('!installpogo'):
            args = message.content.split(" ")
            #file_types = ["ipa"]
            #for attachment in message.attachments:
            #    if any(attachment.filename.lower().endswith(file) for file in file_types):
            #        await message.channel.send('Uploading File...')
            #        await attachment.save(attachment.filename)
            #        await message.channel.send('Uploading Complete...')
            bundle_id, version = parse_ipa(IPAFile)
            await message.channel.send('```\nInstalling '+bundle_id+' '+version+'...```')
            MyOut = subprocess.Popen([IDeviceMobileDir+'ideviceinstaller', '-u', devices.get(args[1]), '--install', IPAFile],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = MyOut.communicate()
            await message.channel.send('```\n'+stdout.decode("utf-8")+'```')
    except TypeError as E:
        print(E)
        await message.channel.send('```\n'+E+'```')

@Client.event
async def on_ready():
    print('Logged In:')
    print(Client.user.name)
    print(Client.user.id)
    print('------------------')

Client.run(ClientToken)
