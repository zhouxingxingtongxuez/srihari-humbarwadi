import argparse


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_feature_maps',
                        type=int,
                        required=True,
                        help='Number of feature maps')

    parser.add_argument('--s_first',
                        type=float,
                        required=True,
                        help='Scale on first feature map')

    parser.add_argument('--smin',
                        type=float,
                        required=True,
                        help='Scale on second feature map')

    parser.add_argument('--smax',
                        type=float,
                        required=True,
                        help='Scale on last feature map')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = _parse_args()

    smin = args.smin * 100
    smax = args.smax * 100
    m = args.num_feature_maps - 1
    scales = [args.s_first]

    for k in range(1, m+2):
        sl = smin + (smax - smin)//(m - 1) * (k - 1)
        scales.append(sl/100)

    print(scales)
