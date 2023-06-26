# Create Subnet Like Pro

> A subnet, short for subnetwork, is a logical subdivision of an IP network. It is created by partitioning a larger network into smaller, more manageable network segments. Subnets play a crucial role in IP address management, network segmentation, security, performance, routing efficiency, and network scalability. They provide a structured and organized approach to network design and management, enabling efficient utilization of resources and improved network functionality.


### Multiple subnets overlapping is a common issue. To ensure that multiple subnets do not overlap their IP address ranges, you can follow these steps:

1. **Determine the total available address space:** Calculate the total number of IP addresses available in the address space you're working with. This will depend on the IP address format you're using (IPv4 or IPv6) and the address range allocated to your network.

2. **Divide the available address space among the subnets:** Divide the total available address space among the number of subnets you need. If you have N subnets, divide the total available address space by N to determine the size of each subnet.

3. **Determine the subnet mask length for each subnet:** Calculate the subnet mask length for each subnet based on the size determined in the previous step. The formula to calculate the subnet mask length is `32 - log2(subnet size)`. This will give you the number of bits to reserve for the network portion of the IP address.

4. **Assign non-overlapping IP address ranges to each subnet:** Start with a network address for the first subnet and increment the network address by the size of each subnet. For example, if your first subnet has a size of 256 addresses, the next subnet's network address would start from the next available address after the first subnet's range. Continue this process for each subnet, ensuring that the ranges do not overlap.

5. **Define the `ip_cidr_range` for each subnet:** Combine each subnet's network address with its corresponding subnet mask length to form the `ip_cidr_range` for that subnet. The `ip_cidr_range` represents the network address followed by a slash and the subnet mask length.

### Let's have some real life scenario

1. Consider we have a total address space of `192.168.0.0/16` (IPv4) and we want to create `4` subnets with equal-sized address ranges.
2. We have `65,536 (2^16)` IPv4 addresses.
3. As we want to create 4 subnets with equal-sized address ranges, each subnet wil contain `65,536/4 = 16,384` addresses.
4. We will calculate the subnet mask length based on the subnet size. Using the formula `32 - log2(subnet size)`, we find that `32 - log2(16384) = 18`. So, each subnet will have a subnet mask length of `18 bits`, **leaving 14 bits for the host portion of the IP address**.
5. Converting `192.168.0.0` to binary `11000000.10101000.00000000.00000000`. Each IP address has 4 parts, its called octate.
6. As we know from 4th step `14 bits` require for each subnet.
7. First subnet ip range will be  `192.168.0.0` to `192.168.63.255` (`11000000.10101000.00000000.00000000` to `11000000.10101000.00111111.11111111` 14 bit from left to right)
8. So, `192.168.63.255` is reserved for first subnet. Next subnet should be allowcated from `192.168.64.0` because `255 (2^8)` is the max for a octate.
9. Second subnet will be start `192.168.64.0` to `192.168.127.255` (`11000000.10101000.01000000.00000000` to `11000000.10101000.01111111.11111111`)
10. Third subnet will be start `192.168.128.0` to `192.168.191.255` (`11000000.10101000.10000000.00000000` to `11000000.10101000.10111111.11111111`)
11. Last subnet will be start `192.168.192.0` to `192.168.255.255` (`11000000.10101000.11000000.00000000` to `11000000.10101000.11111111.11111111`)

### The IP CIDR Ranges for each subnet will be:
- Subnet 1: IP CIDR Range = "192.168.0.0/18"
- Subnet 2: IP CIDR Range = "192.168.64.0/18"
- Subnet 3: IP CIDR Range = "192.168.128.0/18"
- Subnet 4: IP CIDR Range = "192.168.192.0/18"
