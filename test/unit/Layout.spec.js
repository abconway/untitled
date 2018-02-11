import { expect } from 'chai';
import { shallow } from '@vue/test-utils';
import Layout from '@/components/Layout.vue';

describe('Layout.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'Looking at it now, last December.';
    const wrapper = shallow(Layout);
    expect(wrapper.text()).to.include(msg);
  });
});
