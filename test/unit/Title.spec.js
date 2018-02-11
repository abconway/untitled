import { expect } from 'chai';
import { shallow } from '@vue/test-utils';
import Title from '@/components/Title.vue';

describe('Title.vue', () => {
  it('renders a title', () => {
    const msg = 'Hello World!';
    const wrapper = shallow(
      Title,
      {
        propsData: {
          title: msg,
          slugCollision: true,
        },
        methods: {
          getTitles() {
            return [
              {
                id: 1,
                title: msg,
                slug: 'hello-world',
              },
            ];
          },
          slugRandomizer() {
            return 'asdfg';
          },
        },
      },
    );
    expect(wrapper.hasProp('title', msg));
    expect(wrapper.hasProp('slug', 'hello-world-asdfg'));
  });
});
