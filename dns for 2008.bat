@echo off

netsh dnsclient add dnsserver "public" address="dns main ip"
netsh dnsclient add dnsserver "public" index=2 address="dns sub ip"