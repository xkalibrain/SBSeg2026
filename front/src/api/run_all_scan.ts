import { getBanner, getDirectoryScan, getIP, getPorts, getReverseDNS, getSubDNS, getWhatweb, getWhoIs } from "./scan"
import type { ScansAvailable } from "@/types/scan"

export async function RunAllScan(input: string, protocol: 'http' | 'https') {
    input = input.replace(/^https?:\/\//, '')
    const url = new URL(`${protocol}://${input}`)
    const domain = url.hostname
    const domainIsIp = isIP(domain)

    const ip = domainIsIp
        ? domain
        : await getIP(domain)
            .then(response => response.text())
            .then(text => text.split(' ').at(-1)!)

    const promises: Record<ScansAvailable, Promise<Response>> = {
        whatweb: getWhatweb(url.href),
        reverseDNS: getReverseDNS(ip),
        subDNS: getSubDNS(domain),
        whoIs: getWhoIs(ip),
        banner: getBanner(url.href),
        directoryScan: getDirectoryScan(url.origin),
        ports: getPorts(ip)
    }

    return { promises, ip }
}

function isIP(input: string) {
    const ipRegex = /\d{1,3}(\.\d{1,3}){3}/
    return ipRegex.test(input)
}
